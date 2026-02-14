import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="LangChain + Groq Demo", page_icon="🤖")

st.title("🤖 Explain Anything (Groq + LangChain)")
st.write("Enter a topic and get a beginner-friendly explanation.")

# User input
topic = st.text_input("Enter a topic", placeholder="e.g. LangChain, AI, Python")

# Create Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# PromptTemplate
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words for a beginner."
)

# Button
if st.button("Explain"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Thinking... 🤔"):
            response = llm.invoke(
                prompt.format(topic=topic)
            )
            st.success("Explanation:")
            st.write(response.content)
