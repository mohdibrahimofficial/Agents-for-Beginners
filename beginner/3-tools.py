# Reference
# https://platform.openai.com/docs/guides/function-calling?api-mode=responses

import os
from dotenv import load_dotenv
import openai
import requests, json
from pydantic import BaseModel, Field

# Load environment variables from .env file
load_dotenv()

# Using AzureOpenAI model
client = openai.AzureOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPEN_URL")
        )

# Define the Tool
def get_weather(latitude, longitude):
    """This is a publically available API that returns the weather for a given location."""
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]

# Step 1: Call model with get_weather tool defined

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for provided coordinates in celsius.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
                },
                "required": ["latitude", "longitude"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]

system_prompt = "You are a helpful weather assistant."

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What's the weather like in Paris today?"},
]


# This completion useful to get the Lat and Longitude
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
)

completion.model_dump() # Reason to stop is Call tooling

# Step 3: Execute get_weather function

def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)

# For the first time model need tool calling to get the current temperature so calling this API's
# We will also called the second time model because to get the proper response
for tool_call in completion.choices[0].message.tool_calls:
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    messages.append(completion.choices[0].message)

    result = call_function(name, args) # To get the Current temperature using API's
    
    messages.append(
        {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
    ) # Memory

# Step 4: Supply result and call model again

class WeatherResponse(BaseModel):
    temperature: float = Field(
        description="The current temperature in celsius for the given location."
    )
    response: str = Field(
        description="A natural language response to the user's question."
    )

completion_2 = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    response_format=WeatherResponse,
)

completion_2.model_dump() # Reason is Stop

# Step 5: Check model response

final_response = completion_2.choices[0].message.parsed
final_response.temperature
print(final_response.response)