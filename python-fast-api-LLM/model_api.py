from fastapi import FastAPI
from pydantic import BaseModel
from model import *

app = FastAPI()
class Prompt(BaseModel):
    text: str

model = LLM_agent()
@app.post("/api/generate-from-prompt")
async def recvPrompt(prompt: Prompt):
    response = model.generate(prompt.text)+" !!LLM REPONSE MARKER!!"
    return {"response": response}