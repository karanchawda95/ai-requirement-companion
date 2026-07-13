# AI Requirement Companion

AI Requirement Companion is a Python application that helps software teams review and refine requirements from a quality assurance perspective. It uses an LLM to analyze a requirement and highlight ambiguities, risks, missing scenarios, and potential test ideas.

## Overview

This project provides a lightweight Streamlit interface where users can paste a requirement and receive an AI-generated analysis that is useful for:

- identifying unclear or ambiguous language
- surfacing edge cases and hidden assumptions
- spotting risks early in the development lifecycle
- generating initial QA test ideas

## Features

- Simple web-based UI powered by Streamlit
- Requirement analysis through an LLM-backed service
- Configurable model selection via environment variables
- Clean service-oriented structure for future extension

## Tech Stack

- Python 3.12+
- Streamlit
- OpenAI-compatible client for LLM access
- Pydantic settings for environment-based configuration

## Project Structure

```text
src/
  ai_requirement_companion/
    clients/         # LLM client integration
    core/            # configuration and settings
    prompts/         # prompt templates
    services/        # business logic
    streamlit_app.py # Streamlit entrypoint
tests/              # test suite placeholder
```

## Prerequisites

Before running the app, make sure you have:

- Python 3.12 or newer
- An OpenRouter API key (or another compatible API provider configured through the app settings)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd ai-requirement-companion
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the package and dependencies:

   ```bash
   pip install -e .
   ```

## Configuration

Create a `.env` file in the project root with your LLM settings:

```env
OPENROUTER_API_KEY=your_api_key_here
LLM_MODEL=openrouter/free
```

You can adjust the model value to match your provider or preferred model.

## Running the Application

Start the Streamlit app with:

```bash
streamlit run src/ai_requirement_companion/streamlit_app.py
```

Then open the local URL shown by Streamlit in your browser.

## Usage

1. Open the app in your browser.
2. Paste a software requirement into the text area.
3. Click "Analyze Requirement".
4. Review the AI-generated analysis for ambiguity, risks, missing scenarios, and test ideas.

## Development

If you plan to contribute or extend the app:

- keep the UI logic in the Streamlit entrypoint
- place business logic in the service layer
- keep prompt content in the prompts package
- add tests under the tests directory

## License

This project is licensed under the MIT License. See the LICENSE file for details.
