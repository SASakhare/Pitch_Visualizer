from src.prompts.llm_prompt import *
from src.models.google_models import *
from src.models.groq_models import *

from utils.settings import LLM_MODELS_TO_USE


model = LLM_MODELS_TO_USE["model"]


def prompt_generates(user_input: str, context: str, style: str):

    llm_prompt = llm_prompt_for_prompt_gen()

    total_combine_prompt = combine_prompt(
        context=context, user_prompt=user_input, style=style, llm_prompt=llm_prompt
    )

    if model == "gemini":
        prompts = google_inference(input=total_combine_prompt)
    else:
        prompts = groq_inference(input=total_combine_prompt)


    return prompts


# * prompt =[{caption,prompt}]
