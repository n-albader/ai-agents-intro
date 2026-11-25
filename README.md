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
