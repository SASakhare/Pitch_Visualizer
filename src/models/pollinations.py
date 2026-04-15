import asyncio
import httpx
from urllib.parse import quote


def clean_prompt(prompt):
    return quote(prompt)


def generate_image_url(prompt):
    return "https://image.pollinations.ai/prompt/" + clean_prompt(prompt)


async def fetch_image_async(prompt):
    url = generate_image_url(prompt)

    try:
        async with httpx.AsyncClient(timeout=40.0) as client:
            response = await client.get(url)
            return response.content  # raw image bytes

    except Exception as e:
        print(f"Error: {e}")
        return None


async def generate_all_images_pollination(prompts):
    tasks = [
        fetch_image_async(p["prompt"])  # your structure
        for p in prompts
    ]

    results = await asyncio.gather(*tasks)

    return [img for img in results if img is not None]


# images = await generate_all_images(prompts)

# base64_images = [to_base64(img) for img in images]

# return {
#     "images": base64_images
# }

