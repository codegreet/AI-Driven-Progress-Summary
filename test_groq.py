import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Define endpoint and headers
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define payload
payload = {
    "model": "llama-3.3-70b-versatile",  # ✅ Updated working model
    "messages": [
        {"role": "system", "content": "You are an assistant that summarizes progress data."},
        {"role": "user", "content": "Summarize my weekly productivity based on learning data."}
    ],
    "temperature": 0.7
}

print("Sending request to Groq...")

# Send request
response = requests.post(url, headers=headers, json=payload)

# Handle response
if response.status_code == 200:
    data = response.json()
    summary = data["choices"][0]["message"]["content"]
    print("\n✅ Summary generated successfully:\n")
    print(summary)
else:
    print(f"\n❌ Error: {response.status_code}")
    print("Response:", response.text)
