# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     # repo_id="MiniMaxAI/MiniMax-M2.1",
#     # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     # task="conversational"
#     task="text-generation"

# )

# chat = ChatHuggingFace(llm=llm, temperature=0)

# response = chat.invoke("What is the capital of Pakistan?")
# print(response.content)

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation"
# )
# model = ChatHuggingFace(llm=llm, temperature=0.5, max_new_tokens=100)

# chat = model.invoke("What is the capital of Pakistan?")
# print(chat.content)

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"

)

model = ChatHuggingFace(llm=llm, temperature=0, max_new_tokens=100)

response = model.invoke("What is the capital of Pakistan?")

print(response.content)
