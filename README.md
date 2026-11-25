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
