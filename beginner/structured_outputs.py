# Reference
# https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses

import os
from dotenv import load_dotenv
import openai

from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Using AzureOpenAI model
client = openai.AzureOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPEN_URL")
        )

# Define the JSON Model output using Pydantic
class CalendarEvent(BaseModel):
    name: str
    date: str
    day: str
    location: str
    participants: list[str]

# Call the Model
completion = client.beta.chat.completions.parse( # Instead of Create we using Parse and Client.beta
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Extract the Event information"},
                {"role": "user", "content": "Shyam and Mohammed attending the WWDC event at 25th July 2025 at 10am on Paris."}
            ],
            response_format=CalendarEvent
        )

# Parse the Response
event = completion.choices[0].message.parsed # Instead of the Content we are using Parsed

print(event.name)
print(event.date)
print(event.day)
print(event.location)
print(event.participants)