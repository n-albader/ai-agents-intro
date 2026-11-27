
import asyncio
import sys

from dotenv import load_dotenv

load_dotenv()

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.explainer_agent import explainer_agent
from agents.practice_designer_agent import practice_designer_agent
from agents.reviewer_agent import reviewer_agent
from agents.revision_agent import revision_agent

from tools.validation import validate_required_sections
from tools.file_writer import save_markdown_file

from config import validate_configuration


APP_NAME = "ai_study_guide_generator"
USER_ID = "student"

async def execute_agent(agent, prompt):
    """Run an agent and return its text response."""

    session_service = InMemorySessionService()

    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    message = types.Content(
        role="user",
        parts=[types.Part(text=prompt)]
    )

    response_text = []

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session.id,
        new_message=message
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if part.text:
                    response_text.append(part.text)

    return "\n".join(response_text)

def assemble_draft(topic, explanation, practice):
    """Combine the topic, explanation, and practice into a draft."""

    return f"""# Topic

{topic}

{explanation}

{practice}
"""

def assemble_final_markdown(draft, review):
    """Add reviewer comments to the study guide draft."""

    return (
        draft
        + "\n## Review Comments\n\n"
        + review
        + "\n"
    )


async def run_workflow(topic):
    """Run the study guide workflow with one revision attempt."""

    if not topic.strip():
        raise ValueError("Topic cannot be empty.")

    # Step 1: Explainer Agent
    print("\n[1/8] Running Explainer Agent...")

    explanation = await execute_agent(
        explainer_agent,
        f"Explain this programming topic: {topic}"
    )

    if not explanation:
        print("Error: Explainer Agent returned no content.")
        return

    print("Explainer Agent completed.")

    # Step 2: Practice Designer Agent
    print("\n[2/8] Running Practice Designer Agent...")

    practice_prompt = f"""
    Original Topic:
    {topic}

    Explanation from Explainer Agent:
    {explanation}

    Create a beginner-friendly practice exercise.
    """

    practice = await execute_agent(
        practice_designer_agent,
        practice_prompt
    )

    if not practice:
        print("Error: Practice Designer Agent returned no content.")
        return

    print("Practice Designer Agent completed.")

    # Step 3: Assemble the draft
    print("\n[3/8] Assembling Draft Study Guide...")

    draft = assemble_draft(
        topic,
        explanation,
        practice
    )

    # Step 4: Reviewer Agent
    print("\n[4/8] Running Reviewer Agent...")

    review = await execute_agent(
        reviewer_agent,
        f"""
        Review the following study guide draft.

        Identify missing information, unclear explanations,
        and suggestions for improvement.

        Do not rewrite the guide.

        STUDY GUIDE DRAFT:

        {draft}
        """
    )

    if not review:
        print("Error: Reviewer Agent returned no content.")
        return

    print("Reviewer Agent completed.")

    # Step 5: Assemble the first version
    print("\n[5/8] Assembling Initial Study Guide...")

    draft_markdown = assemble_final_markdown(
        draft,
        review
    )

    # Save the first draft
    draft_result = save_markdown_file(
        "output/study_guide_draft.md",
        draft_markdown
    )

    print(draft_result)

    if not draft_result.startswith("File saved successfully:"):
        print("Error: Could not save the initial draft.")
        return

    # Step 6: Validate the first draft
    print("\n[6/8] Validating Initial Draft...")

    validation_result = validate_required_sections(
        draft_markdown
    )

    final_markdown = draft_markdown

    # Step 7: One revision attempt if needed
    if not validation_result["is_valid"]:

        missing_sections = validation_result["missing_sections"]

        print("\nValidation failed. Missing sections:")

        for section in missing_sections:
            print(f"- {section}")

        print("\nRunning Revision Agent (one attempt only)...")

        revision_prompt = f"""
        Revise the following study guide.

        Missing required sections:
        {", ".join(missing_sections)}

        Add the missing sections while preserving
        the existing useful content.

        ORIGINAL STUDY GUIDE:

        {draft_markdown}
        """

        revised_markdown = await execute_agent(
            revision_agent,
            revision_prompt
        )

        if revised_markdown:
            final_markdown = revised_markdown
            print("Revision completed.")
        else:
            print("Revision Agent returned no content.")
            print("Keeping the original draft.")

    else:
        print("Initial validation passed. No revision needed.")

    # Step 8: Final validation and saving
    print("\n[7/8] Running Final Validation...")

    final_validation = validate_required_sections(
        final_markdown
    )

    if final_validation["is_valid"]:
        print("Final validation PASSED.")
    else:
        print("Final validation FAILED.")

        print("Still missing:")

        for section in final_validation["missing_sections"]:
            print(f"- {section}")

    print("\n[8/8] Saving Final Study Guide...")

    final_result = save_markdown_file(
        "output/study_guide_final.md",
        final_markdown
    )

    print(final_result)

    if not final_result.startswith("File saved successfully:"):
        print("Error: Could not save the final study guide.")
        return

    print("\nWorkflow completed.")
    print(
        f"Final validation status: "
        f"{'PASSED' if final_validation['is_valid'] else 'FAILED'}"
    )

def main():
    """Read the topic, validate configuration, and start the workflow."""

    topic = " ".join(sys.argv[1:]).strip()

    if not topic:
        print('Error: Topic cannot be empty.')
        print('Usage: python3 main.py "Python decorators"')
        sys.exit(1)

    try:
        validate_configuration()

        print(f"\nStarting Study Guide Workflow for: {topic}")

        asyncio.run(run_workflow(topic))

    except (ValueError, ConnectionError) as error:
        print(f"\nConfiguration or input error: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"\nWorkflow error: {error}")
        raise


if __name__ == "__main__":
    main()
