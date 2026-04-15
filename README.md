
---
#  **Pitch Visualizer**

- *Convert plain text into visual storyboards using AI.*

---

## 🧠 **What this project does**

Pitch Visualizer takes a paragraph (like a business story or idea) and turns it into a sequence of images with captions — basically a **visual storyboard**.

Instead of just reading text, you can actually _see_ the story.

---

## ✨ Why I built this

A lot of ideas — especially in business or presentations — are hard to explain with just text.

This project tries to solve that by:

- breaking the story into scenes
- generating meaningful visuals
- keeping everything context-aware

---

## ⚙️ How it works (simple flow)

<img src="./image/README/Assessment for AI Intern Role  Darwix AI.png" width="700"/>

---

## 🧩 Tech used

- FastAPI (backend)
- Jinja2 (templates)
- Groq (LLM for prompt generation)
- HuggingFace / Pollinations (image generation)
- asyncio + httpx (for async requests)

---

## 📁 Project structure

```
Pitch_Visualizer/

├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore

├── src/
│   ├── models/
│   │   ├── groq_models.py
│   │   ├── huggingface_models.py
│   │   ├── pollinations.py
│   │   └── google_models.py
│   │
│   ├── prompts/
│   │   ├── prompt_service.py
│   │   └── llm_prompt.py
│   │
│   └── images/

├── templates/
│   ├── index.html
│   └── storyboard.html

├── static/
│   └── style.css

├── utils/
│   ├── settings.py
│   └── utils.py
```

---

## 🚀 **Running the project**

### 1. Clone

```
git clone https://github.com/SASakhare/Pitch_Visualizer.git
cd Pitch_Visualizer
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Create `.env` file

In the root folder:

```
.env
```

Add:

```
GROQ_API_KEY=your_key
HF_TOKEN=your_token
GOOGLE_API_KEY=your_key
```

---

### 4. Run

```
fastapi dev
```

Open:

```
http://127.0.0.1:8000
```

---

## 🎮 How to use

- Enter your story (a few lines or paragraph)
- Choose:
  - context (business, AI, etc.)
  - style (cinematic, sketch, etc.)

- Click generate
- You’ll get a storyboard with images + captions

---

## ⚙️ Model settings (important)

All model selection is controlled from:

```
utils/settings.py
```

Example:

```python
IMAGE_MODELS_TO_USE = {
    "model": "huggingface"
}
```

You can change it to:

```python
"model": "pollinations"
```

---

## 🔐 API key note

- HuggingFace → requires API key
- Groq → requires API key
- Pollinations → no key needed

Make sure your `.env` file is set up properly.

---

## ⚠️ Things to keep in mind

- Image generation can be slow sometimes (depends on API)
- Pollinations may take retries
- HuggingFace gives better consistency but needs a key

---

## 📸 Output

Each scene includes:

- one generated image
- one caption
- aligned with the original story

---

## 🔮 Possible improvements

- export storyboard as PDF / PPT
- better UI (animations, loaders)
- character consistency across scenes
- real-time streaming

---

## 🎯 Final note

This project is mainly about combining:

- prompt engineering
- async backend
- multiple AI services

into one clean pipeline.

---

## 🧾 One-line description

AI tool that converts text stories into visual storyboards using LLMs and image generation models.

---
