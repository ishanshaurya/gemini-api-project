# Gemini API Project

**Repo:** https://github.com/ishanshaurya/gemini-api-project
**Project spec:** https://roadmap.sh/projects/openai-api-python

A hands-on project exploring the Google Gemini API in Python — starting from a single hardcoded API call and scaling it up, stage by stage, into a configurable, interactive script. Built by following a structured phase-based learning roadmap (see `Phase2_Gemini_API_Project.pdf` reference).

## What it does

Takes a prompt from the user at runtime, sends it to Gemini, and returns a response — with full control over how "creative" or "focused" the model is, how long its answer can be, and what persona it responds as.

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

You'll be prompted for:
- **Your prompt** — the question you want answered
- **Temperature** (0.0–2.0, default 0.7) — how varied vs. deterministic the response is
- **Max tokens** (default 1000) — hard length limit on the response

## How the project scaled up (stage by stage)

### Phase 1 — Get a response from the API
Simplest possible version: one fixed prompt, hardcoded in the script, sent straight to `genai.Client().models.generate_content()`. Goal was just proving the API connection worked end-to-end.

### Phase 2 — Make it interactive and configurable
Phase 1 could only ever answer one question. Phase 2 turned it into an actual tool, in four small steps:

1. **Live input** — swapped the hardcoded prompt for `input()`, so any question can be asked without touching the code.
2. **Runtime parameters** — added `temperature` and `max_tokens` as user inputs (with sensible defaults if left blank), so response randomness and length are controllable per-run instead of fixed.
3. **Structured config** — passed both parameters into the API call via `types.GenerateContentConfig(...)`, the SDK's bundled settings object.
4. **System instruction** — gave the model a standing persona (`system_instruction`) that shapes every response's tone, separate from the actual question being asked.

Each step was verified independently before moving to the next — e.g. confirming the same prompt produces different tone with vs. without the system instruction.

## Concepts learned (in the order I hit them)

1. **Client/SDK setup** — using `google-genai` + `python-dotenv` to keep the API key out of source code.
2. **Tokens vs. words** — a token is a subword chunk from the model's tokenizer, not a word or character (`"unbelievable"` → 3 tokens).
3. **Autoregressive generation** — the model generates one token at a time, feeding its own output back in as input for the next step. This is *why* `max_output_tokens` is a hard cutoff, not a polite suggestion — the server just stops calling the model once the count is hit.
4. **Sampling & temperature** — the model outputs a full probability distribution over next-tokens, not a single answer. Temperature controls how that distribution gets sampled: low = picks the top candidate almost every time (deterministic), high = flattens the distribution so unlikely tokens get a real shot (varied, sometimes incoherent). At `temperature=0`, this becomes greedy decoding — always the top token.
5. **The softmax mechanic behind it** — `probability(token) = exp(logit / temperature) / sum(exp(all_logits / temperature))`. Dividing by a small number stretches gaps apart (peaked); dividing by a large number flattens them.
6. **Misconception correction** — temperature doesn't add knowledge or fix wrong answers. It only reshuffles which *already-plausible* phrasing gets picked.
7. **System instruction vs. user message** — both are plain text, but the model is trained to treat them with different priority. System instruction = standing behavioral rule (persona, tone); user message = the specific thing being asked right now.
8. **Config objects over loose kwargs** — `GenerateContentConfig` bundles optional settings into one object that the SDK serializes into the API request body, instead of passing a dozen raw arguments.
9. **Debugging with `finish_reason`** — `response.candidates[0].finish_reason` tells you *why* generation stopped (`MAX_TOKENS` vs `STOP`), which is the fast way to confirm a cutoff was hit by design, not a bug.

## Requirements

- Python 3.9+
- Gemini API key

## What's next

Phase 3: multi-turn conversation — giving the model memory across turns by resending accumulated conversation history with each request.
