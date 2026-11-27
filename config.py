
import os
import json
from urllib.request import urlopen
from urllib.error import URLError


MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "openai").lower()

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "openai/gpt-4o-mini"
)

OLLAMA_API_BASE = os.getenv(
    "OLLAMA_API_BASE",
    "http://localhost:11434"
)


def validate_configuration():
    """Validate the selected model provider configuration."""

    if MODEL_PROVIDER == "openai":
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError(
                "OPENAI_API_KEY is missing. "
                "Add it to your .env file."
            )

    elif MODEL_PROVIDER == "ollama":
        if not MODEL_NAME.startswith("ollama_chat/"):
            raise ValueError(
                "For Ollama, MODEL_NAME must use this format: "
                "ollama_chat/model-name"
            )

        try:
            with urlopen(
                f"{OLLAMA_API_BASE}/api/tags",
                timeout=3
            ) as response:
                data = json.loads(response.read().decode("utf-8"))

        except (URLError, TimeoutError, OSError) as error:
            raise ConnectionError(
                "Cannot connect to Ollama. "
                "Make sure Ollama is running."
            ) from error

        available_models = [
            model["name"]
            for model in data.get("models", [])
        ]

        requested_model = MODEL_NAME.split("/", 1)[1]

        if requested_model not in available_models:
            raise ValueError(
                f"Ollama model '{requested_model}' is not available. "
                "Download it using: ollama pull "
                f"{requested_model}"
            )

    else:
        raise ValueError(
            f"Unsupported MODEL_PROVIDER: {MODEL_PROVIDER}. "
            "Choose 'openai' or 'ollama'."
        )

