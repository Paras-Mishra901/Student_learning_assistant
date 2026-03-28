import os
import io
import time
import requests
from PIL import Image, ImageDraw
from dotenv import load_dotenv

load_dotenv()
def _get_hf_api_key():
    try:
        import streamlit as st
        return st.secrets.get("HUGGINGFACE_API_KEY", os.getenv("HUGGINGFACE_API_KEY"))
    except Exception:
        return os.getenv("HUGGINGFACE_API_KEY")


HF_API_KEY = _get_hf_api_key()

HF_IMAGE_MODELS = [
    "black-forest-labs/FLUX.1-schnell",
    "runwayml/stable-diffusion-v1-5",
    "stabilityai/stable-diffusion-xl-base-1.0"
]

WORKING_MODEL_CACHE = None


def _fallback_image(message="Image generation failed"):
    img = Image.new("RGB", (1024, 1024), color=(18, 18, 28))
    draw = ImageDraw.Draw(img)
    text = (
        f"{message}\n\n"
        f"Check:\n"
        f"1. HUGGINGFACE_API_KEY\n"
        f"2. Internet connection\n"
        f"3. Model access / rate limits\n"
        f"4. Hugging Face API status"
    )
    draw.multiline_text((50, 100), text, fill=(255, 255, 255), spacing=10)
    return img


def _style_prompt(prompt: str, style: str) -> str:
    style_map = {
        "Realistic": "photorealistic, ultra detailed, 8k, highly realistic",
        "Anime": "anime style, vibrant colors, detailed illustration",
        "Cartoon": "cartoon style, bold outlines, colorful digital illustration",
        "Fantasy": "fantasy art, magical atmosphere, epic scenery",
        "Cyberpunk": "cyberpunk style, neon lights, futuristic city",
        "3D Render": "3d render, octane render, cinematic lighting",
        "Watercolor": "watercolor painting, soft brush strokes",
        "Pixel Art": "pixel art, retro 16-bit style, crisp pixels",
        "Studio Ghibli-like": "whimsical anime background, hand-painted style"
    }
    style_text = style_map.get(style, "high quality digital art, detailed")
    return f"{prompt}, {style_text}"


def _check_model_available(model_id: str) -> bool:
    if not HF_API_KEY:
        return False
    try:

        headers = {
            "Authorization": f"Bearer {HF_API_KEY}",
            "User-Agent": "Mozilla/5.0"
        }
        info_url = f"https://huggingface.co/api/models/{model_id}"
        response = requests.get(info_url, headers=headers, timeout=20)
        return response.status_code == 200
    except Exception:
        return False


def _get_best_available_model() -> str:
    global WORKING_MODEL_CACHE
    if WORKING_MODEL_CACHE:
        return WORKING_MODEL_CACHE
    for model_id in HF_IMAGE_MODELS:
        if _check_model_available(model_id):
            WORKING_MODEL_CACHE = model_id
            return model_id
    return HF_IMAGE_MODELS[0]


def _parse_error(response):
    try:
        error_data = response.json()
        return error_data.get("error", f"HTTP {response.status_code}")
    except:
        return f"HTTP {response.status_code}"


def _generate_with_model(model_id: str, final_prompt: str):

    api_url = f"https://router.huggingface.co/hf-inference/models/{model_id}"


    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python-Requests/2.31.0"
    }

    payload = {
        "inputs": final_prompt,
        "options": {"wait_for_model": True}
    }

    response = requests.post(api_url, headers=headers, json=payload, timeout=180)


    if response.status_code == 200:
        if 'image' in response.headers.get('content-type', ''):
            return Image.open(io.BytesIO(response.content)).convert("RGB")
        else:
            raise Exception("API returned success but no image data.")


    if response.status_code == 503:
        time.sleep(10)  # Wait for model to load
        response = requests.post(api_url, headers=headers, json=payload, timeout=180)
        if response.status_code == 200:
            return Image.open(io.BytesIO(response.content)).convert("RGB")

    raise Exception(_parse_error(response))


def generate_image(prompt: str, style: str = "Realistic"):
    try:
        if not HF_API_KEY:
            return _fallback_image("Missing HUGGINGFACE_API_KEY")

        final_prompt = _style_prompt(prompt.strip(), style)
        primary_model = _get_best_available_model()
        model_attempts = [primary_model] + [m for m in HF_IMAGE_MODELS if m != primary_model]

        last_error = None
        for model_id in model_attempts:
            try:
                return _generate_with_model(model_id, final_prompt)
            except Exception as e:
                last_error = f"{model_id}: {str(e)}"
                continue

        return _fallback_image(f"Models failed. Last error: {last_error}")

    except Exception as e:
        return _fallback_image(f"Error: {str(e)}")