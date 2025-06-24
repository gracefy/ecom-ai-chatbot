import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env variables once
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Global reusable client instance
openai = OpenAI(api_key=OPENAI_API_KEY)
