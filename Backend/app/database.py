from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# MongoDB URI and DB name
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "aptech_freelance")
SECRET_KEY = os.getenv("SECRET_KEY", "wswebsolution_super_secure_786")

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
