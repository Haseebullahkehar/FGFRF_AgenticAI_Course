from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# initialize the mode 
model = ChatGroq(
     model="llama-3.1-8b-instant",
    temperature=0.7
)

messages = [
    SystemMessage(content="You are a helpful, polite and knowledgeable assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)