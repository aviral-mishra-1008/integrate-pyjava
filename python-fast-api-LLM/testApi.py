from fastapi import FastAPI
from pydantic import BaseModel
from model import *

app = FastAPI()
class Prompt(BaseModel):
    text: str

model = Pythia_model()
@app.post("/api/generate-from-prompt")
async def recvPrompt(prompt: Prompt):
    response = model.generate(prompt.text)+"!!LLM REPONSE!!"
    return {"response": response}