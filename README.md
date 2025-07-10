# AI Agent

AI Agent is a Python command-line AI agent using the Google Gemini API, function calling, and iterative prompting.  
This project is part of the [Boot.dev guided project series](https://www.boot.dev/courses/build-ai-agent-python).

## Features

- Uses Google Gemini API for content generation
- Supports function calling and tool use through function definitions
- Iterative prompt handling with configurable maximum iterations
- Verbose mode for debugging prompt/response token usage
- Can view file contents, write to files, and run files in a given directory

## Usage

1. (Recommended) Use [uv](https://github.com/astral-sh/uv) for fast and reproducible Python environment management:

    ```bash
    uv venv
    # On Unix/macOS
    source .venv/bin/activate
    # On Windows
    .venv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    uv pip install -r requirements.txt
    ```

3. Set your Gemini API key in a `.env` file:

    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

4. Run the agent:

    ```bash
    python main.py <your prompt here> [--verbose]
    ```

    - Replace `<your prompt here>` with your desired input prompt.
    - Add `--verbose` to enable detailed token usage output.
