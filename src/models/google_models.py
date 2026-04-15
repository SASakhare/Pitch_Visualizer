from google import genai
import os
from dotenv import load_dotenv
from utils.settings import LLM_MODELS
load_dotenv()


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()




def google_inference(input: str):

    response = client.models.generate_content(
        model=LLM_MODELS['gemini']["model"], # type: ignore
        contents=input,
    )

    result = response.text
    prompts = ast.literal_eval(result)  # type: ignore

    return prompts
