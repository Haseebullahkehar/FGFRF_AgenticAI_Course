# from dotenv import load_dotenv
# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# # Initialize Gemini model
# model = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0.3
# )

# st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")

# if st.button("Summarize"):
#     if user_input:
#         result = model.invoke(user_input)
#         st.write(result.content)

# from dotenv import load_dotenv
# import streamlit as st
# from langchain_groq import ChatGroq

# load_dotenv()

# # Initialize Groq model
# model = ChatGroq(
#     model="llama-3.1-8b-instant",  # or llama-3.1-70b-versatile
#     temperature=0.3
# )

# st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")

# if st.button("Summarize"):
#     if user_input:
#         result = model.invoke(user_input)
#         st.write(result.content)



from langchain_groq import ChatGroq 
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()

# initialize the model 
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.content)
































# # from langchain_google_genai import GoogleGenerativeAI
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import streamlit as st 
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# model = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.3
# )

# st.header("Research Tool")

# # user_input = st.text_input("Enter your prompt")
# # creating drop down menu for user input
# paper_input = st.selectbox("Select Research Paper Name", ["Select...", "Attention Is All You Need", 
# "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "CodeOriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# # template 
# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following 
# specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1. Mathematical Details: - Include relevant mathematical equations if present in the paper. - Explain the mathematical concepts using simple, intuitive code snippets 
# where applicable. 
# 2. Analogies: - Use relatable analogies to simplify complex ideas. 
# If certain information is not available in the paper, respond with: "Insufficient 
# information available" instead of guessing. 
# Ensure the summary is clear, accurate, and aligned with the provided style and 
# length.
# """,
# input_variables=["paper_input", "style_input", "length_input"]

# )

# # fill the placeholder 
# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })
# # create summarize button 
# if st.button("Summarize"):
#         result = model.invoke(prompt.format)
#         st.write(result.content)



   