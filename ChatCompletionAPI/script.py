import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages =[ 
        {
            "role": "system",
            "content": "You are a helpful assistant that can answer questions and help with tasks."
        },
        {
            "role": "user",
            "content": "Hello, how are you?"
        },
        {
            "role": "assistant",
            "content": "Hello! I'm just a computer program, so I don't have feelings, but I'm here and ready to help you. How can I assist you today?"
        },
        {
            "role": "user",
            "content": "What is the capital of France?"
        },
    ]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.6,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response.choices[0].message.content)
