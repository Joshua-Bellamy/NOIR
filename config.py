import os
from dotenv import load_dotenv

# Load environment variables from the .env file into memory
load_dotenv()

# Read the OpenRouter API Key from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Fail immediately with a clear error if the key is missing
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found. Make sure it's set in your .env file")
