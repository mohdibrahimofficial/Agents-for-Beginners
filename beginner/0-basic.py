import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Using AzureOpenAI model
client = openai.AzureOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPEN_URL")
        )

# Direct Open AI sample code
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You're a helpful assistant"},
                {"role": "user", "content": "Write a joke about the python programming"}
            ],
        )

response = completion.choices[0].message.content

print(response)