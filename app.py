from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio

# import your functions
from src.prompt_service import prompt_generates
from utils.settings import IMAGE_MODELS_TO_USE
from fastapi.staticfiles import StaticFiles
# from src.image.pollinations import generate_all_images, to_base64

from src.models.huggingface_models import generate_all_images_huggingface
from src.models.pollinations import generate_all_images_pollination
from utils.utils import to_base64

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# HOME PAGE
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(request=request, name="index.html")


# GENERATE STORYBOARD
@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    text: str = Form(...),
    context: str = Form(...),
    style: str = Form(...),
):

    # STEP 1 — LLM (prompts + captions)
    data = prompt_generates(
        user_input=text, context=context, style=style
    )  # * prompt =[{caption,prompt}]

    # STEP 2 — images

    if IMAGE_MODELS_TO_USE["model"] == "pollinations":

        images = await generate_all_images_pollination(data)
    else:
        images = await generate_all_images_huggingface(data)

    base64_images = [to_base64(img) for img in images]

    # STEP 3 — combine
    storyboard = []
    for item, img in zip(data, base64_images):
        storyboard.append({"caption": item["caption"], "image": img})

    return templates.TemplateResponse(
        request=request,
        name="storyboard.html",  # type: ignore
        context={
            "request": request,
            "storyboard": storyboard,
            "context": context,
            "style": style,
        },  # type: ignore
    )
