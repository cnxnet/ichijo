from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

# Obtener las claves de API desde las variables de entorno
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

class DocumentRequest(BaseModel):
    prompt: str

@app.post("/generate-document")
def generate_document(request: DocumentRequest):
    """
    Endpoint para generar documentos basados en IA.
    """
    if not DEEPSEEK_API_KEY:
        return {"error": "API Key de DeepSeek no configurada"}

    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
        json={"model": "deepseek-chat", "messages": [{"role": "user", "content": request.prompt}]}
    )

    return response.json()
