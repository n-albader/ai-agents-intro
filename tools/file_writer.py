from pathlib import Path

def save_markdown_file(file_path: str, content: str) -> str:
    """Save Markdown content to a file."""

    path = Path(file_path)

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return f"File saved successfully: {path}"

    except OSError as error:
        return (
            f"Error saving file '{path}': {error}. "
            "Check the file path and folder permissions."
        )
