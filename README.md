# AI Agents in Python

## Description

AI Agents in Python is a multi-agent system that generates programming study guides for beginner students.

The project uses Google ADK and LiteLLM to coordinate three AI agents in a sequential workflow.

Each agent has a specific responsibility:

1. Explain a programming topic.
2. Design a practice exercise based on the explanation.
3. Review the generated study guide and provide feedback.

The final study guide is assembled, validated, and saved as a Markdown file.

## Requirements

- Python 3
- An OpenAI API key
- Internet connection
- The following Python packages:
  - `google-adk`
  - `litellm`
  - `python-dotenv`

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/n-albader/ai-agents-intro
cd ai-agents-intro
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The project uses OpenAI through LiteLLM.

Create a `.env` file in the project root:

```env
MODEL_PROVIDER=openai
MODEL_NAME=openai/gpt-4o-mini
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own OpenAI API key.

The configuration variables are:

- `MODEL_PROVIDER`: Selects the model provider.
- `MODEL_NAME`: Specifies the model used by the agents.
- `OPENAI_API_KEY`: Authenticates requests to the OpenAI API.

Never commit the `.env` file or expose your API key.

The `.env` file is excluded from version control through `.gitignore`.

## How to Run

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the application with a programming topic:

```bash
python3 main.py "Python decorators"
```

The application executes the following sequential workflow:

1. Receives the programming topic.
2. Runs the Explainer Agent.
3. Runs the Practice Designer Agent using the explanation.
4. Assembles the draft study guide.
5. Runs the Reviewer Agent.
6. Assembles the final Markdown document.
7. Validates the required sections.
8. Saves the study guide to `output/study_guide.md`.

## Example Input

```text
Python decorators
```

## Example Output

The generated file is saved at:

`output/study_guide.md`

Example of the generated Markdown structure:

```markdown
# Topic

Python decorators

## Simple Explanation

A decorator is a function that adds functionality
to another function without changing its original code.

## Key Concepts

- Functions
- Higher-order functions
- Wrapper functions

## Example

A simple Python decorator example.

## Practice Exercise

Create a decorator that prints a message
before calling a function.

## Common Mistakes

- Forgetting to return the wrapper function.

## Review Comments

### Missing Information

No major missing information.

## Final Summary

Decorators help extend function behavior
without modifying the original function.
```

The actual generated content may vary depending on the model response.

## Project Structure

```text
ai-agents-intro/
│
├── agents/
│   ├── __init__.py
│   ├── explainer_agent.py
│   ├── practice_designer_agent.py
│   └── reviewer_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── file_writer.py
│   └── validation.py
│
├── output/
│   └── study_guide.md
│
├── data/
│   └── topic_examples.json
│
├── config.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Agents

### 1. Explainer Agent

File: `agents/explainer_agent.py`

Responsible for explaining the programming topic in simple language.

It generates:

- Simple Explanation
- Key Concepts
- Example
- Common Mistakes
- Final Summary

### 2. Practice Designer Agent

File: `agents/practice_designer_agent.py`

Receives the original topic and the explanation from the Explainer Agent.

It creates a beginner-friendly practice exercise with:

- Practice Exercise
- Expected Input
- Expected Output
- Hints

### 3. Reviewer Agent

File: `agents/reviewer_agent.py`

Receives the assembled draft study guide and evaluates its quality.

It reviews:

- Missing Information
- Unclear Explanations
- Suggestions for Improvement
- Recommendation

## Tools

### 1. File Writer Tool

File: `tools/file_writer.py`

Provides the `save_markdown_file()` function.

Its responsibilities are:

- Create the output directory if it does not exist.
- Save the final study guide as a Markdown file.
- Handle file-writing errors and return readable error messages.

### 2. Validation Tool

File: `tools/validation.py`

Provides the `validate_required_sections()` function.

It checks whether the study guide contains all required Markdown sections.

It returns:

- `is_valid`: Indicates whether all required sections exist.
- `missing_sections`: Lists any missing sections.

## Self-Validation Checklist

- [x] Three agents have separate responsibilities.
- [x] Agents execute in a sequential workflow.
- [x] The Practice Designer Agent uses the Explainer Agent's output.
- [x] The Reviewer Agent reviews the assembled draft.
- [x] The Validation Tool checks required sections.
- [x] The File Writer Tool saves the Markdown document.
- [x] Model configuration is managed through environment variables.
- [x] The project includes basic error handling.
- [x] API keys are excluded from version control.

## Reflection

### 1. What is the difference between a direct LLM call and an AI agent?

A direct LLM call sends a prompt to a language model and receives a response.

An AI agent has a defined role, instructions, and the ability to perform specific tasks as part of a larger workflow. Agents can use tools and work with the outputs of other agents.

### 2. What role does each agent have in your system?

- **Explainer Agent:** Explains the programming topic and generates beginner-friendly learning content.
- **Practice Designer Agent:** Uses the explanation to create a practical exercise.
- **Reviewer Agent:** Reviews the draft and provides feedback and improvement suggestions.

Each agent focuses on one responsibility, making the workflow easier to organize and maintain.

### 3. What role does each tool have in your system?

- **Validation Tool:** Checks that all required sections are present in the generated Markdown.
- **File Writer Tool:** Saves the final study guide to the output directory.

These tools handle supporting operations instead of making the agents responsible for every task.

### 4. What was the most difficult part of the project?

The most difficult part was coordinating the agents in the correct sequence and passing the output of one agent to the next.

It was also important to assemble the generated content correctly and ensure that the final Markdown document contained all required sections.

### 5. What limitation did you observe when using your selected model?

The selected model, `gpt-4o-mini`, can generate different responses for the same topic.

It may not always follow the requested Markdown structure exactly or include every required section. This is why the project uses a separate validation tool.

The generated technical content also needs human review because an AI-generated explanation or code example may contain inaccuracies.

## Known Limitations

- The project depends on an internet connection and access to the OpenAI API.
- API usage may incur costs depending on the account and usage.
- Generated explanations and exercises may vary between runs.
- The model may omit or incorrectly format required sections.
- The validation tool checks section headings, not the technical accuracy of the content.
- The Reviewer Agent provides suggestions but does not automatically correct the study guide.
- The project uses a sequential workflow, so each step waits for the previous agent to finish.
- The model runs through the OpenAI API rather than locally on the computer. Local hardware is used to run the Python application, not to host the model.

