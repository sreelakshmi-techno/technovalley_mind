from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

print("BASE_DIR =", BASE_DIR)

env_path = BASE_DIR / ".env"

print("ENV EXISTS =", env_path.exists())
print("ENV PATH =", env_path)

load_dotenv(env_path)

print("KEY =", os.getenv("GEMINI_API_KEY"))