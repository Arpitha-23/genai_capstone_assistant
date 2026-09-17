from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF file.
    """

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def clean_text(text):
    """
    Clean unnecessary whitespace from extracted text.
    """

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:

        line = line.strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def chunk_text(
    text,
    chunk_size=1000,
    overlap=200
):
    """
    Split document text into overlapping chunks.

    Example:

    Chunk 1: characters 0 - 1000
    Chunk 2: characters 800 - 1800
    Chunk 3: characters 1600 - 2600
    """

    if not text:
        return []

    chunks = []

    start = 0

    text_length = len(text)

    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks