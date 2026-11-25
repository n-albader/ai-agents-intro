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

### Run the Agent

```bash
python3 main.py "Python decorators"
