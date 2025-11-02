import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env file")

def summarize_progress(week_data):
    text = "\n".join([f"{d['day']}: {d['hours_studied']} hrs, {d['tasks_completed']} tasks" for d in week_data])

    prompt = f"""
    You are an AI progress analyst.
    Analyze the following 7-day learning data and write a short, 2-3 sentence motivational summary
    describing productivity trends, improvements, or dips.

    Data:
    {text}
    """

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",  # ✅ Correct active model
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 200
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        res_json = response.json()

        if "choices" in res_json and len(res_json["choices"]) > 0:
            summary = res_json["choices"][0]["message"]["content"]
            return summary.strip()
        elif "error" in res_json:
            return f"LLM Error: {res_json['error'].get('message', 'Unknown error')}"
        else:
            return "Unexpected response from Groq API."

    except Exception as e:
        return f"Error generating summary: {e}"
