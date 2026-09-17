import os

from dotenv import load_dotenv
from google import genai


# --------------------------------------------------
# Load API key
# --------------------------------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not configured."
    )


# --------------------------------------------------
# Gemini Client
# --------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# --------------------------------------------------
# Embedding Model
# --------------------------------------------------

EMBEDDING_MODEL = "gemini-embedding-001"


# --------------------------------------------------
# Create Embedding
# --------------------------------------------------

def create_embedding(text):
    """
    Convert text into a numerical vector.
    """

    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return result.embeddings[0].values


# --------------------------------------------------
# Create Multiple Embeddings
# --------------------------------------------------

def create_embeddings(text_chunks):
    """
    Create embeddings for multiple document chunks.
    """

    embeddings = []

    for chunk in text_chunks:

        embedding = create_embedding(chunk)

        embeddings.append(embedding)

    return embeddings


# --------------------------------------------------
# Embed User Question
# --------------------------------------------------

def create_query_embedding(question):
    """
    Convert a user's question into an embedding.
    """

    return create_embedding(question)