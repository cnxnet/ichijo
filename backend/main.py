from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

DEEPSEEK_API_KEY = os.getenv("sk-800ec655dc774fe9bae1c8fe6b6ed50f")

class DocumentRequest(BaseModel):
    prompt: str

@app.post("/generate-document")
def generate_document(request: DocumentRequest):
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {sk-800ec655dc774fe9bae1c8fe6b6ed50f}"},
        json={"model": "deepseek-chat", "messages": [{"role": "user", "content": request.prompt}]}
    )
    return response.json()
