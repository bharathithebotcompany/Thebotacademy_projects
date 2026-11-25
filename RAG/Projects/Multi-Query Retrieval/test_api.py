import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
print("Key",os.getenv("OPENAI_API_KEY"));
# Create client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simple test request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What is the capital of Pakistan?"}
    ],
    max_tokens=200
)

print(response.choices[0].message.content)