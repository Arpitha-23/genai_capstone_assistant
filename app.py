import streamlit as st

from core.llm import generate_response

from core.prompts import (
    GENERAL_ASSISTANT_PROMPT,
    STUDY_ASSISTANT_PROMPT,
    CAREER_ASSISTANT_PROMPT,
)

from rag.document_processor import (
    extract_text_from_pdf,
    clean_text,
    chunk_text,
)

from rag.embeddings import (
    create_embeddings,
    create_query_embedding,
)

from rag.vector_store import VectorStore

from rag.qa import answer_question

from agent.agent import AIAgent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="GenAI Study & Career Assistant",
    page_icon="🤖",
    layout="wide",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 25px;
    }

    .feature-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "vector_store" not in st.session_state:
    st.session_state.vector_store = VectorStore()


if "document_name" not in st.session_state:
    st.session_state.document_name = None


if "document_chunks" not in st.session_state:
    st.session_state.document_chunks = []


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if "ai_agent" not in st.session_state:
    st.session_state.ai_agent = AIAgent()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🤖 GenAI Study & Career Assistant</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="subtitle">
    An all-in-one Generative AI application combining
    LLMs, Prompt Engineering, RAG, Embeddings,
    Vector Search, AI Agents and Tool Calling.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Assistant Mode")

    mode = st.radio(
        "Choose a mode:",
        [
            "General AI",
            "Study Assistant",
            "Career Assistant",
            "Chat With Documents",
            "AI Agent",
        ],
    )

    st.divider()

    # ========================================================
    # DOCUMENT UPLOAD
    # ========================================================

    st.header("📄 Document Upload")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"],
    )

    if uploaded_file is not None:

        if (
            st.session_state.document_name
            != uploaded_file.name
        ):

            with st.spinner(
                "Processing document..."
            ):

                try:

                    # ----------------------------------------
                    # Extract text
                    # ----------------------------------------

                    raw_text = extract_text_from_pdf(
                        uploaded_file
                    )

                    # ----------------------------------------
                    # Clean text
                    # ----------------------------------------

                    cleaned_text = clean_text(
                        raw_text
                    )

                    # ----------------------------------------
                    # Chunk text
                    # ----------------------------------------

                    chunks = chunk_text(
                        cleaned_text,
                        chunk_size=1000,
                        overlap=200,
                    )

                    if not chunks:

                        st.error(
                            "No readable text was found "
                            "in this PDF."
                        )

                    else:

                        # ------------------------------------
                        # Create embeddings
                        # ------------------------------------

                        with st.spinner(
                            "Creating document embeddings..."
                        ):

                            embeddings = create_embeddings(
                                chunks
                            )

                        # ------------------------------------
                        # Build vector store
                        # ------------------------------------

                        st.session_state.vector_store.build(
                            embeddings,
                            chunks,
                        )

                        # ------------------------------------
                        # Save document information
                        # ------------------------------------

                        st.session_state.document_name = (
                            uploaded_file.name
                        )

                        st.session_state.document_chunks = (
                            chunks
                        )

                        st.success(
                            "Document processed successfully!"
                        )

                except Exception as e:

                    st.error(
                        f"Document processing error: {str(e)}"
                    )

    # ========================================================
    # DOCUMENT INFORMATION
    # ========================================================

    if st.session_state.document_name:

        st.divider()

        st.write(
            f"📄 **Document:** "
            f"{st.session_state.document_name}"
        )

        st.write(
            f"🧩 **Chunks:** "
            f"{len(st.session_state.document_chunks)}"
        )


    st.divider()

    # ========================================================
    # EXAMPLE QUESTIONS
    # ========================================================

    st.header("💡 Example Questions")

    if mode == "General AI":

        st.caption(
            "What is Generative AI?"
        )

        st.caption(
            "Explain machine learning simply."
        )

        st.caption(
            "What is an LLM?"
        )


    elif mode == "Study Assistant":

        st.caption(
            "Explain DBMS normalization."
        )

        st.caption(
            "Explain operating systems simply."
        )

        st.caption(
            "Give me 5 interview questions."
        )


    elif mode == "Career Assistant":

        st.caption(
            "How can I prepare for a software internship?"
        )

        st.caption(
            "What skills should a CSE student learn?"
        )

        st.caption(
            "How should I prepare for technical interviews?"
        )


    elif mode == "Chat With Documents":

        st.caption(
            "Summarize this document."
        )

        st.caption(
            "What are the important points?"
        )

        st.caption(
            "Explain this document simply."
        )


    elif mode == "AI Agent":

        st.caption(
            "Calculate 25 * 18"
        )

        st.caption(
            "Add Complete my project to my tasks"
        )

        st.caption(
            "Show my tasks"
        )

        st.caption(
            "What is the current time?"
        )


    st.divider()

    # ========================================================
    # CLEAR CHAT
    # ========================================================

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
    ):

        st.session_state.chat_history = []

        st.session_state.ai_agent = AIAgent()

        st.rerun()


# ============================================================
# MODE INFORMATION
# ============================================================

if mode == "General AI":

    st.info(
        "💬 General AI — Ask questions and get "
        "AI-powered responses."
    )

elif mode == "Study Assistant":

    st.info(
        "📚 Study Assistant — Get beginner-friendly "
        "explanations and study guidance."
    )

elif mode == "Career Assistant":

    st.info(
        "💼 Career Assistant — Get guidance for "
        "internships, resumes and interviews."
    )

elif mode == "Chat With Documents":

    st.info(
        "📄 Chat With Documents — Upload a PDF and "
        "ask questions using RAG."
    )

elif mode == "AI Agent":

    st.info(
        "🤖 AI Agent — The agent understands your task "
        "and decides when to use available tools."
    )


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.chat_history:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# USER INPUT
# ============================================================

user_input = st.chat_input(
    "Ask your question..."
)


if user_input:

    # ========================================================
    # DISPLAY USER MESSAGE
    # ========================================================

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):

        st.markdown(
            user_input
        )


    # ========================================================
    # ASSISTANT RESPONSE
    # ========================================================

    with st.chat_message("assistant"):

        with st.spinner(
            "🤔 Thinking..."
        ):

            try:

                # ==================================================
                # AI AGENT
                # ==================================================

                if mode == "AI Agent":

                    answer = (
                        st.session_state.ai_agent.run(
                            user_input
                        )
                    )


                # ==================================================
                # CHAT WITH DOCUMENTS / RAG
                # ==================================================

                elif mode == "Chat With Documents":

                    if (
                        not st.session_state.document_chunks
                        or
                        st.session_state.vector_store.index
                        is None
                    ):

                        answer = (
                            "📄 Please upload and process "
                            "a PDF before asking questions "
                            "about the document."
                        )

                    else:

                        # ------------------------------------------
                        # Create query embedding
                        # ------------------------------------------

                        query_embedding = (
                            create_query_embedding(
                                user_input
                            )
                        )

                        # ------------------------------------------
                        # Retrieve + Generate
                        # ------------------------------------------

                        answer = answer_question(
                            question=user_input,
                            vector_store=(
                                st.session_state.vector_store
                            ),
                            query_embedding=query_embedding,
                            top_k=3,
                        )


                # ==================================================
                # STUDY ASSISTANT
                # ==================================================

                elif mode == "Study Assistant":

                    answer = generate_response(
                        user_input,
                        STUDY_ASSISTANT_PROMPT,
                    )


                # ==================================================
                # CAREER ASSISTANT
                # ==================================================

                elif mode == "Career Assistant":

                    answer = generate_response(
                        user_input,
                        CAREER_ASSISTANT_PROMPT,
                    )


                # ==================================================
                # GENERAL AI
                # ==================================================

                else:

                    answer = generate_response(
                        user_input,
                        GENERAL_ASSISTANT_PROMPT,
                    )


                # ==================================================
                # DISPLAY RESPONSE
                # ==================================================

                st.markdown(
                    answer
                )


                # ==================================================
                # SAVE RESPONSE
                # ==================================================

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )


            except Exception as e:

                error_message = (
                    f"An error occurred: {str(e)}"
                )

                st.error(
                    error_message
                )

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )