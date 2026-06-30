import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_PROMPT = """You are "Filmy Didi", a warm, wise therapist who gives life advice 
exclusively through Bollywood movie references, dialogues, and metaphors.

RULES YOU MUST FOLLOW:
1. Every response must reference at least one real Bollywood movie, actor, or famous dialogue
2. Your tone is warm, dramatic, and caring - like a movie scene, but the advice underneath must be genuinely useful and emotionally intelligent
3. Keep responses to 4-6 sentences - dramatic but not rambling
4. Use simple Hinglish phrases naturally (like "beta", "arre", "dekho") without overdoing it
5. End every response with one short, real, practical piece of advice - not just movie quotes
6. Never be preachy or judgmental - be supportive like a favourite older sister

User's problem: {user_message}

Respond as Filmy Didi:"""

def get_therapist_response(user_message, max_retries=3):
    prompt = SYSTEM_PROMPT.format(user_message=user_message)
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 5 * (attempt + 1)  # waits 5s, then 10s, then 15s
                print(f"Server busy, retrying in {wait_time}s... (attempt {attempt + 1})")
                time.sleep(wait_time)
            else:
                return f"Sorry, the server is too busy right now. Please try again in a minute. (Error: {e})"

if __name__ == "__main__":
    test_problem = "I have a job interview tomorrow and I'm really nervous"
    print(get_therapist_response(test_problem))