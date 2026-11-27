# AI Study Guide Generator

## Description

AI Study Guide Generator is a Python application that uses multiple AI agents to create structured programming study guides in Markdown format.

## Project Structure

- `agents/`: Contains the AI agents.
- `tools/`: Contains deterministic Python tools.
- `output/`: Stores generated study guides.
- `data/`: Stores example topics.
- `main.py`: Application entry point.

## Technologies

- Python
- Google ADK
- LiteLLM
- OpenAI

## Model Provider

This project uses OpenAI API through LiteLLM.

The model is configured using environment variables.
An OpenAI API key is required to run the agents.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python3 main.py
```

## Reflection

This project introduces AI agent development, tool integration, and multi-agent workflows using Python.

## Model Environment Setup

### Model Provider

This project uses OpenAI API as its language model provider instead of running a local model through Ollama.

### Architecture

Google ADK → LiteLLM → OpenAI API

### Python Environment

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
MODEL_PROVIDER=openai
MODEL_NAME=openai/gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key
```

Never commit the `.env` file to GitHub.

### Test the Model

The model connection can be tested using LiteLLM before integrating it with Google ADK.

### Model Configuration

- Provider: OpenAI
- Model: gpt-4o-mini
- Connector: LiteLLM
- Agent Framework: Google ADK

### Limitations

The application requires an internet connection and a valid OpenAI API key. API usage may incur costs.

## Explainer Agent

The Explainer Agent is the first AI agent in this project.

### Responsibilities

- Explain programming topics.
- Identify key concepts.
- Provide simple code examples.

### Model Configuration

- Provider: OpenAI
- Model: gpt-4o-mini
- Framework: Google ADK
- Connector: LiteLLM

### Example

Input:

Python decorators

Output:

The agent generates a structured Markdown
explanation containing:

1. Explanation
2. Key Concepts
3. Simple Example

# Python Decorators

## 1. Explanation

A Python decorator is a special type of function that can modify or enhance another function. It allows you to add extra functionality to an existing function without changing its code.

You can think of a decorator as a wrapper around a function.

## 2. Key Concepts

- **Function:** A reusable block of code that performs a specific task.
- **Higher-order Function:** A function that takes another function as an argument or returns a function.
- **Wrapper Function:** A function defined inside a decorator that calls the original function and adds extra behavior.
- **@ Symbol:** Used to apply a decorator to a function.

## 3. Simple Example

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
```

### Explanation of the Code

1. **my_decorator:** Takes a function `func` as an argument.
2. **wrapper:** Prints a message before and after calling the original function.
3. **@my_decorator:** Applies the decorator to `say_hello`.
4. **say_hello():** Calls the decorated function, which executes the wrapper.

### Expected Output

```text
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

### Run the Agent

```bash
python3 main.py "Python decorators"

## Markdown File Writer

The project includes a file-writing tool in `tools/file_writer.py`.

The `save_markdown_file()` function:
- Accepts a file path and Markdown content.
- Creates the parent directory if it does not exist.
- Saves the content as a UTF-8 Markdown file.
- Handles file-writing errors gracefully.

### Output

The Explainer Agent saves its generated explanation to:

```text
output/study_guide.md
```

### Usage

Run the agent with a programming topic:

```bash
python3 main.py "Python decorators"
```

The generated Markdown explanation is saved automatically to `output/study_guide.md`.

## Markdown Validation Tool

The project includes a validation tool in `tools/validation.py`.

The `validate_required_sections()` function checks whether the generated Markdown study guide contains all eight required sections:

- Topic
- Simple Explanation
- Key Concepts
- Example
- Practice Exercise
- Common Mistakes
- Review Comments
- Final Summary

The function returns:
- `is_valid`: A Boolean indicating whether all required sections exist.
- `missing_sections`: A list of sections that are missing.

The validation tool runs after the Explainer Agent generates its response and before the Markdown file is saved.

### Validation Result

The program reports whether the generated study guide contains all required sections and identifies any missing headings.

## Practice Designer Agent

The project includes a Practice Designer Agent in `agents/practice_designer_agent.py`.

Its responsibility is to generate a beginner-friendly programming exercise based on:

- The original programming topic.
- The explanation generated by the Explainer Agent.

The agent produces:

- A practical exercise.
- Expected input, when applicable.
- Expected output, when applicable.
- One or two hints.

The Practice Designer Agent does not rewrite the explanation. Its output is combined with the Explainer Agent's output to create the final Markdown study guide.

### Multi-Agent Workflow

1. The Explainer Agent generates the topic explanation.
2. The Practice Designer Agent receives the original topic and explanation.
3. The Practice Designer Agent creates a practice exercise.
4. Both outputs are combined into `output/study_guide.md`.
5. The Validation Tool checks the required sections.

## Reviewer Agent

The project includes a Reviewer Agent in `agents/reviewer_agent.py`.

Its responsibility is to review the study guide generated by the Explainer Agent and Practice Designer Agent.

The Reviewer Agent receives the current study guide draft and produces:

- Missing information.
- Unclear or ambiguous explanations.
- Specific suggestions for improvement.
- An approval or revision recommendation.

The Reviewer Agent does not rewrite the entire study guide.

### Multi-Agent Workflow

1. The Explainer Agent generates the explanation.
2. The Practice Designer Agent creates a beginner-friendly exercise.
3. The Reviewer Agent reviews the combined draft.
4. Review comments are added to the final Markdown document.
5. The Validation Tool checks the required sections.
6. The final study guide is saved to `output/study_guide.md`.

## Sequential Workflow

The project uses a sequential multi-agent workflow to generate programming study guides.

### Workflow Steps

1. **Topic Input:** The user provides a programming topic.
2. **Explainer Agent:** Generates the explanation, key concepts, example, common mistakes, and final summary.
3. **Practice Designer Agent:** Receives the original topic and explanation to create a beginner-friendly exercise with expected input, expected output, and hints.
4. **Draft Study Guide:** Combines the topic, explanation, and practice exercise.
5. **Reviewer Agent:** Reviews the draft and provides missing information, unclear explanations, improvement suggestions, and a recommendation.
6. **Final Markdown Assembly:** Adds the review comments to the draft.
7. **Validation Tool:** Checks whether all required sections exist.
8. **Save Markdown Tool:** Saves the final study guide to `output/study_guide.md`.

### Run the Workflow

```bash
python3 main.py "Python decorators"
```

The final Markdown study guide is saved in the `output/` directory.


## Configuration

The project supports two model providers through LiteLLM:

### OpenAI

Add the following settings to your `.env` file:

```env
MODEL_PROVIDER=openai
MODEL_NAME=openai/gpt-4o-mini
OPENAI_API_KEY=your_api_key_here
```

### Ollama

Make sure Ollama is installed and running, then download a model:

```bash
ollama pull llama3.2
```

Configure `.env`:

```env
MODEL_PROVIDER=ollama
MODEL_NAME=ollama_chat/llama3.2
OLLAMA_API_BASE=http://localhost:11434
```

Never commit your `.env` file or expose API keys.

## Troubleshooting

### Empty Topic

**Problem:** No topic was provided.

**Solution:** Run the program with a topic:

```bash
python3 main.py "Python decorators"
```

### Missing OpenAI API Key

**Problem:** `OPENAI_API_KEY is missing`.

**Solution:** Add a valid API key to your `.env` file.

### Ollama Is Not Running

**Problem:** Cannot connect to Ollama.

**Solution:** Start the Ollama application or run:

```bash
ollama serve
```

### Ollama Model Is Not Available

**Problem:** The requested model is not installed.

**Solution:** Download it:

```bash
ollama pull llama3.2
```

### File-Writing Error

**Problem:** The study guide cannot be saved.

**Solution:** Check the output folder path and file permissions.

### Validation Failure

**Problem:** One or more required Markdown sections are missing.

**Solution:** Check the missing section names in the terminal output and inspect:

```bash
cat output/study_guide.md
```

The project saves the generated guide even when validation fails, so it can be inspected and corrected.

