import streamlit as st
import ollama

# --- Streamlit Page Config ---
st.set_page_config(page_title="AI Code Review Bot", page_icon="🤖")
st.title("🤖 AI Code Review Bot (Ollama + CodeLlama)")

st.write("Paste your code below and get an AI-powered review. The bot will remember past reviews during this session.")

# --- Session Memory ---
if "history" not in st.session_state:
    st.session_state["history"] = []

# --- User Input ---
user_code = st.text_area("Your Code:", height=250, placeholder="Paste Python/JS/Java code here...")

if st.button("Review Code"):
    if user_code.strip():
        # Build conversation context
        history_text = "\n\n".join([
            f"User: {h['user']}\nBot: {h['bot']}"
            for h in st.session_state["history"]
        ])
        
        review_prompt = f"""
You are a senior software engineer. Review the following code for bugs, improvements, and best practices.
Keep feedback clear, structured, and constructive.

Conversation so far:
{history_text}

Code to review:
{user_code}
"""
        # --- Call Ollama Model ---
        response = ollama.chat(model="codellama", messages=[
            {"role": "user", "content": review_prompt}
        ])
        bot_reply = response["message"]["content"]

        # Save to memory
        st.session_state["history"].append({"user": user_code, "bot": bot_reply})

        # Display result
        st.subheader("AI Review:")
        st.write(bot_reply)
    else:
        st.warning("Please paste some code first!")

# --- Show History ---
with st.expander("Conversation History"):
    for i, chat in enumerate(st.session_state["history"], 1):
        st.markdown(f"**Q{i}:**")
        st.code(chat["user"], language="python")
        st.markdown(f"**AI Review {i}:** {chat['bot']}")
