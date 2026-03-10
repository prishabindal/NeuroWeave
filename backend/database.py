import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.neuro_weave_db # Database name

async def save_quiz_result(user_id, topic, score):
    await db.performance.insert_one({"user_id": user_id, "topic": topic, "score": score})