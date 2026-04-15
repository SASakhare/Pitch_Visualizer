from io import BytesIO
import base64

def to_base64(img):
    # If already bytes (Pollinations)
    if isinstance(img, bytes):
        return base64.b64encode(img).decode()

    # If PIL image (HuggingFace)
    from io import BytesIO
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()