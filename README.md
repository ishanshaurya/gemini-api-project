# gemini-api-project

**Repo:** https://github.com/ishanshaurya/gemini-api-project
**Project spec:** https://roadmap.sh/projects/openai-api-python

Minimal Python script demonstrating the Gemini API via `google-genai`.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey).

## Usage

```bash
python main.py
```

Sends a prompt to `gemini-2.5-flash` and prints the response.

## Requirements

- Python 3.9+
- Gemini API key
