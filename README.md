🔹 Overview

This project is an AI-powered code review assistant that analyzes source code, identifies bugs, suggests improvements, and provides best practices. It is powered by Ollama running the CodeLlama model, and has a web interface built with Streamlit.

Unlike OpenAI-based bots, this works entirely for free, running models locally, with no API costs.

🔹 Features

✅ Code Review – Paste code and get AI-driven review suggestions
✅ Memory – The bot remembers past reviews in the same session, allowing context-aware discussions
✅ Streamlit Web App – User-friendly interface accessible in the browser
✅ Offline & Free – Runs locally with Ollama (CodeLlama), no paid APIs
✅ Expandable History – See past questions and AI responses in an organized view

🔹 Tech Stack

Backend AI Model: Ollama + CodeLlama (local LLM optimized for coding)

Frontend: Streamlit (Python framework for interactive apps)

Memory Management: st.session_state (stores conversation history)

Language: Python

Optional: Can be extended with ChromaDB or FAISS for long-term memory

🔹 How It Works

User pastes code into the text box.

The app builds a prompt including:

The current code snippet

Conversation history from earlier reviews

This prompt is sent to Ollama (CodeLlama) for analysis.

The model generates feedback on bugs, improvements, and coding best practices.

The response is displayed in the app, and also stored in session memory for continuity.
🔹 Possible Extensions

File Upload: Allow .py, .js, .java file uploads for review.

Multi-Language Detection: Auto-detect whether the code is Python, JS, Java, etc.

Lint Integration: Combine AI suggestions with tools like pylint or flake8.

Persistent Memory: Store reviews in a database (ChromaDB/Redis).

Team Mode: Multiple users can collaborate and review the same code in real time.

🔹 Why This Project is Valuable

Shows you can integrate local AI models (Ollama) into practical tools.

Demonstrates Streamlit UI development.

Proves knowledge of LLM prompting, context handling, and memory.

Very relevant for roles in AI, ML, or software engineering tooling.
