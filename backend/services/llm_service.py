import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

MODEL = os.getenv("MODEL", "gemini-2.5-flash")


def get_llm():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            f"GEMINI_API_KEY not found in {BASE_DIR / '.env'}"
        )

    return ChatGoogleGenerativeAI(
        model=MODEL,
        google_api_key=api_key,
        temperature=0,
    )CD..
    