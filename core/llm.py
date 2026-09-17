import os
import time

from dotenv import load_dotenv
from google import genai


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not configured. "
        "Please add it to your .env file."
    )


# --------------------------------------------------
# Gemini Client
# --------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# --------------------------------------------------
# Gemini Model
# --------------------------------------------------

MODEL_NAME = "gemini-3.6-flash"


# --------------------------------------------------
# Generate Response
# --------------------------------------------------

def generate_response(
    prompt: str,
    system_instruction: str | None = None
) -> str:
    """
    Generate a response using Google Gemini.

    Automatically retries temporary 503/429 errors.
    """

    config = {
        "temperature": 0.4
    }

    if system_instruction:
        config["system_instruction"] = system_instruction

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=config
            )

            if response.text:
                return response.text

            return "I couldn't generate a response."

        except Exception as e:

            error_text = str(e)

            # Temporary server/quota errors
            if (
                "503" in error_text
                or "UNAVAILABLE" in error_text
                or "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
            ):

                if attempt < max_retries - 1:

                    wait_time = 2 ** attempt

                    time.sleep(wait_time)

                    continue

            return f"Error generating response: {error_text}"

    return "The Gemini service is temporarily unavailable. Please try again."