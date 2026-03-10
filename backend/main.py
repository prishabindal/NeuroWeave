from fastapi import FastAPI, UploadFile, File
from openai import AzureOpenAI
import os
from database import get_weak_areas
from prompts import create_adaptive_prompt
import azure.cognitiveservices.speech as speechsdk

app = FastAPI()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

@app.post("/analyze-notes")
async def analyze_notes(user_id: str, file: UploadFile = File(...)):
    # 1. Logic to extract text from image using GPT-4o Vision
    # 2. Call Azure OpenAI with the image
    # 3. Retrieve weak areas from database
    weak_areas = await get_weak_areas(user_id)
    # 4. Generate structured content
    return {"message": "Notes processed successfully"}


def text_to_speech(text):
    speech_config = speechsdk.SpeechConfig(
        subscription=os.getenv("AZURE_SPEECH_KEY"), 
        region=os.getenv("AZURE_SPEECH_REGION")
    )
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    result = synthesizer.speak_text_async(text).get()
    return result