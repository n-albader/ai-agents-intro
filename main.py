
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

    if not topic.strip():
        raise ValueError("Topic cannot be empty.")

async def run_workflow(topic):
    """Run the complete sequential study guide workflow."""

    # Step 1: Explainer Agent
    print("\n[1/7] Running Explainer Agent...")

    explanation = await execute_agent(
        explainer_agent,
        f"Explain this programming topic: {topic}"
    )

    if not explanation:
        print("Error: Explainer Agent returned no content.")
        return

    print("Explainer Agent completed.")

    # Step 2: Practice Designer Agent
    print("\n[2/7] Running Practice Designer Agent...")

    practice_prompt = f"""
    Original Topic:
    {topic}

    Explanation from Explainer Agent:
    {explanation}

    Create a beginner-friendly practice exercise based on
    the topic and explanation.
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
    print("\n[3/7] Assembling Draft Study Guide...")

    draft = assemble_draft(
        topic,
        explanation,
        practice
    )

    print("Draft Study Guide assembled.")

    # Step 4: Reviewer Agent
    print("\n[4/7] Running Reviewer Agent...")

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

    # Step 5: Assemble final Markdown
    print("\n[5/7] Assembling Final Markdown...")

    final_markdown = assemble_final_markdown(
        draft,
        review
    )

    print("Final Markdown assembled.")

    
    # Step 6: Validate the final Markdown
    print("\n[6/7] Validating Study Guide...")

    validation_result = validate_required_sections(
        final_markdown
    )

    if validation_result["is_valid"]:
        print("Validation successful: all required sections exist.")
    else:
        print("Validation failed. Missing sections:")

        for section in validation_result["missing_sections"]:
            print(f"- {section}")

        print(
            "The generated guide will still be saved "
            "so you can inspect and fix it."
        )

    # Step 7: Save Markdown file
    print("\n[7/7] Saving Study Guide...")

    result = save_markdown_file(
        "output/study_guide.md",
        final_markdown
    )

    print(result)


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
