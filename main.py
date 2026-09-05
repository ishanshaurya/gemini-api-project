from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

user_prompt = input("Enter your prompt: ")

temperature = float(input("Enter temperature (0.0-2.0, default 0.7): ") or "0.7")
max_token = int(input("Max tokens (default 1000): ") or "1000")

system_instruction = "You are a sarcastic teenager who finds every question boring and answers as briefly as possible."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt,
    config=types.GenerateContentConfig(
        temperature=temperature,
        max_output_tokens=max_token,
        system_instruction=system_instruction
    )
)

print(response.text)