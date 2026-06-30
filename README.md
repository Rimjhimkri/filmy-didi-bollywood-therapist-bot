# 🎬 Filmy Didi — Bollywood Therapist Bot

A chatbot that gives genuinely useful life advice wrapped in Bollywood movie 
references, dialogues, and dramatic flair — like having a wise, filmy older 
sister who's seen every movie ever made.

## Live Demo

![Filmy Didi Chat Interface](screenshot.png)

*Run locally — see Setup below*

## What it does

Send it any problem — stress, heartbreak, failure, anxiety — and Filmy Didi 
responds with real emotional support, woven through references to classic 
and modern Bollywood films, while always ending with one practical, 
actionable piece of advice.

## Example

**Input:** "I failed an important exam and feel like giving up"

**Output:**
> Arre beta, this feeling of wanting to give up, it's like that moment in 
> *3 Idiots* when Rancho reminds everyone, "All izz well," even when things 
> seem bleakest. You've faced a temporary setback, not a permanent defeat, na?
> Just like how in *Chak De! India*, Kabir Khan used his past failure not to 
> quit, but to build an even stronger dream, you too have the spirit of a 
> true champion within you. This isn't the final reel, mere pyaare, but just 
> an interval, giving you time to gather your strength for the second half!
>
> Practical advice: Allow yourself a day to feel your emotions, then identify 
> one small, actionable step you can take towards your goal.

## Tech Stack

- **Backend:** Python, Flask
- **AI Model:** Google Gemini 2.5 Flash (via `google-genai` SDK)
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Approach:** Custom system prompt engineering with structured behavioral rules

## How it works

The core of this project is a carefully engineered system prompt that enforces:
- Consistent persona (warm, dramatic, Bollywood-themed)
- Mandatory real movie/dialogue references for authenticity
- Response length constraints (4-6 sentences) to avoid rambling
- A mandatory practical takeaway, so the bot is genuinely useful — not just funny
- Natural Hinglish phrasing for cultural authenticity

The API includes input validation (empty message handling, length limits) and 
automatic retry logic with exponential backoff to handle transient API failures 
gracefully.

## API Usage

**Endpoint:** `POST /ask`

**Request:**
```json
{
  "message": "I am stressed about money"
}
```

**Response:**
```json
{
  "your_problem": "I am stressed about money",
  "filmy_didi_says": "Arre beta, this stress about money..."
}
```

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it and install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with your `GOOGLE_API_KEY` (get one free at [aistudio.google.com](https://aistudio.google.com))
5. Run the server: `python app.py`
6. Open `http://127.0.0.1:5000` in your browser

## Built by

Rimjhim Kumari — MCA Graduate | Full Stack Developer
[LinkedIn](https://www.linkedin.com/in/rimjhim-kumari-098302374) · [GitHub](https://github.com/Rimjhimkri)