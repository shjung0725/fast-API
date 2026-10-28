from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Text Analyzer Demo")


class TextInput(BaseModel):
    text: str


# Health check endpoint to confirm the service is running
@app.get("/health")
def health():
    return {"status": "ok"}


# Placeholder "model": counts words and characters (no real AI model yet)
@app.post("/predict")
def predict(data: TextInput):
    words = data.text.split()
    return {
        "word_count": len(words),
        "char_count": len(data.text),
        "label": "long" if len(words) > 10 else "short",
    }
