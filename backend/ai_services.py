import os
from openai import AzureOpenAI
import azure.cognitiveservices.speech as speechsdk

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

def get_explanation(image_url):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": [{"type": "text", "text": "Analyze these handwritten notes."}, {"type": "image_url", "image_url": {"url": image_url}}]}]
    )
    return response.choices[0].message.content

def text_to_speech(text):
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("AZURE_SPEECH_KEY"), region="eastus")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    return synthesizer.speak_text_async(text).get()