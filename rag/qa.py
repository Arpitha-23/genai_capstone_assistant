from core.llm import generate_response
from core.prompts import RAG_PROMPT


def answer_question(
    question,
    vector_store,
    query_embedding,
    top_k=3
):
    """
    Retrieve relevant document chunks and
    generate an answer using Gemini.
    """

    results = vector_store.search(
        query_embedding,
        top_k=top_k
    )

    if not results:

        return (
            "I could not find relevant information "
            "in the uploaded document."
        )

    context_parts = []

    for result in results:

        context_parts.append(
            result["document"]
        )

    context = "\n\n".join(
        context_parts
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    return generate_response(
        prompt
    )