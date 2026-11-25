import asyncio
import sys

from dotenv import load_dotenv

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

load_dotenv()

from agents.explainer_agent import explainer_agent


APP_NAME = "ai_study_guide_generator"
USER_ID = "student"


async def run_agent(topic):
    """Run the explainer agent with a programming topic."""

    session_service = InMemorySessionService()

    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    runner = Runner(
        agent=explainer_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    message = types.Content(
        role="user",
        parts=[types.Part(text=topic)]
    )

    print(f"\nGenerating study explanation for: {topic}\n")

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session.id,
        new_message=message
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if part.text:
                    print(part.text)


def main():
    """Read the topic from command-line arguments."""

    if len(sys.argv) < 2:
        print("Usage: python3 main.py 'Programming Topic'")
        sys.exit(1)

    topic = " ".join(sys.argv[1:])

    asyncio.run(run_agent(topic))


if __name__ == "__main__":
    main()
