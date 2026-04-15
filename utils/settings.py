import os

# -----------------------------
# LLM CONFIG
# -----------------------------


LLM_MODELS_TO_USE = {"model": "groq"}  # "gemini"


LLM_MODELS = {
    "groq": {
        "model": "llama-3.3-70b-versatile",
    },
    "gemini": {
        "model": "gemini-3-flash-preview",
    },
}


# -----------------------------
# IMAGE CONFIG
# -----------------------------
# IMAGE_PROVIDER = os.getenv("IMAGE_PROVIDER", "pollinations")


IMAGE_MODELS_TO_USE = {
    "model": "pollinations",
}


IMAGE_MODELS = {
    "pollinations": {"type": "url"},
    "huggingface": {
        "model": "zai-org/GLM-Image",
        "provider": "zai-org",
    },
}
