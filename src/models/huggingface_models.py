import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from utils.settings import IMAGE_MODELS
import asyncio

load_dotenv()


client = InferenceClient(
    provider=IMAGE_MODELS["huggingface"]["provider"], # type: ignore
    api_key=os.environ["HF_TOKEN"],
)


async def generate_image_async(prompt):
    try:
        loop = asyncio.get_event_loop()

        img = await loop.run_in_executor(
            None,
            lambda: client.text_to_image(prompt, model=IMAGE_MODELS["huggingface"]["model"])
        )

        return img  # return PIL image directly

    except Exception as e:
        print(f"Error: {e}")
        return None


async def generate_all_images_huggingface(prompts):
    tasks = [generate_image_async(p) for p in prompts]

    results = await asyncio.gather(*tasks)

    # remove failed ones
    return [img for img in results if img is not None]





# images = await generate_all_images(prompts)

# base64_images = [to_base64(img) for img in images]
# return {
#     "images": base64_images
# }



