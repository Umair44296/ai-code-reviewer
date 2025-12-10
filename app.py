import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(
    model_name="mistralai/devstral-2512:free",
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
)


prompt = """
You are an AI Code Reviewer.

Your task is to carefully analyze the provided code snippet and evaluate it for correctness, readability, efficiency, and potential errors.

After deep analysis, produce your response in the following structured format:

Summary:
- Provide a concise explanation of what the code does.

Potential_Issues:
- List any logical errors, syntax problems, or bad practices found in the code.

Suggestions:
- Offer clear and actionable recommendations for improving performance, clarity, or maintainability.
"""

st.title("AI Code Reviewer")
st.write("Paste your Python code below and click **Review Code** to get AI feedback.")

user_code = st.text_area("Your Code:", height=220, placeholder="Paste your Python code here...")

if st.button("Review Code"):
    if not user_code.strip():
        st.warning("⚠️ Please paste some code first.")
    else:
        with st.spinner("Analyzing your code..."):
            full_prompt = f"{prompt}\n\nReview this code:\n```python\n{user_code}\n```"
            response = llm.invoke(full_prompt)

        st.subheader("🔍 Review Result:")
        st.markdown(response.content)
