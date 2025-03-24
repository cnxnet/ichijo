from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Carga .env (solo en local)
app = FastAPI()

# Obtiene la clave DESDE VARIABLES DE ENTORNO (no hardcodeada)
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

class DocumentRequest(BaseModel):
    prompt: str

@app.post("/generate-document")
def generate_document(request: DocumentRequest):
    if not DEEPSEEK_API_KEY:
        return {"error": "API Key de DeepSeek no configurada"}

    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},  # Usa la variable
        json={"model": "deepseek-chat", "messages": [{"role": "user", "content": request.prompt}]}
    )
    return response.json()
