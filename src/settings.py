import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")
PORT: int = int(os.environ.get("PORT"))
REDIS: str = os.environ.get("REDIS")
API_TOKEN: str = os.environ.get("API_TOKEN")
CACHE_TTL: int = int(os.environ.get("CACHE_TTL"))
