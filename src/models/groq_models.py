import os
from dotenv import load_dotenv
from groq import Groq
import ast

from utils.settings import LLM_MODELS

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def groq_inference(input: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input,
            }
        ],
        model=LLM_MODELS["groq"]["model"], # type: ignore
    )

    result = chat_completion.choices[0].message.content
    prompts = ast.literal_eval(result) # type: ignore

    return prompts




