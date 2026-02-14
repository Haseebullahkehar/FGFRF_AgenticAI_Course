# # # from langchain_groq import ChatGroq
# # # # from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # # Create Groq model
# # # model = ChatGroq(
# # # #     model="llama-3.1-8b-instant",
# # # #     temperature=0.7
# # # # )

# # # # # chat_history = [
# # # # #     SystemMessage(content="You are a helpful assistant")
# # # # # ]

# # # # chat_history = []

# # # # print("Groq Chatbot 🤖 (type 'exit' to quit)\n")

# # # # while True:
# # # #     user_input = input("You: ")
# # # #     # chat_history.append(HumanMessage(content=user_input))
# # # #     chat_history.append(content=user_input)


# # # #     if user_input.lower() == "exit":
# # # #         print("Goodbye 👋")
# # # #         break

# # # #     result = model.invoke(user_input)
# # # #     # result = model.invoke(chat_history) # 2
# # # #     # chat_history.append(AIMessage(content=result.content)) # 3
# # # #     # chat_history.append(content=result.content) #2

# # # #     print("AI:", result.content)

# # # # print(chat_history)



# # # from langchain_groq import ChatGroq
# # # from dotenv import load_dotenv

# # # from langchain_groq import ChatGroq 
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # model = ChatGroq(
# # #     model="llama-3.1-8b-instant",
# # #     temperature=0.6

# # # )

# # # print("Groq Chatbot 🤖 (type 'exit' to quit)\n")

# # # while True:
# # #     user_input = input('You: ')
# # #     if user_input.lower() == "exit":
# # #         print("Goodbye 👋")
# # #         break

# # # #     response = model.invoke(user_input)
# # # #     print("AI:", response.content)


# # from langchain_groq import ChatGroq
# # from dotenv import load_dotenv
# # load_dotenv()

# # # Initialize Groq model
# # model = ChatGroq(
# #     model="llama-3.1-8b-instant",
# #     temperature=0.7
# # )

# # print("Groq Chatbot 🤖 (type 'exit' to quit)\n")

# # while True:
# #     user_input = input("You: ")

# #     if user_input.lower() == "exit":
# #         print("Goodbye 👋")
# #         break

# #     # Direct invocation (no chat history, no message objects)
# #     response = model.invoke(user_input)

# #     print("AI:", response.content)


# from langchain_groq import ChatGroq 
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.6
# )

# chat_history = []

# print("Groq Chatbot 🤖 (type 'exit' to quit)\n")

# while True:
#     user_input = input('You: ').strip()
#     if user_input.lower() == "exit":
#         print("Goodbye 👋")
#         break

#     # store user input as plain text
#     chat_history.append(user_input)

#     # send full history to model
#     response = model.invoke(chat_history)

#     print("AI:", response.content)

#     # store AI reply as plain text
#     chat_history.append(response.content)

# print(chat_history)










# #     # chat history  
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# # Create Groq model
# model = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.7
# )

# chat_history = []

# print("Groq Chatbot 🤖 (type 'exit' to quit)\n")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         print("Goodbye 👋")
#         break

#     # store user input as plain text
#     chat_history.append(user_input)

#     # send full history to model
#     result = model.invoke(chat_history)

#     print("AI:", result.content)

#     # store AI reply as plain text
#     chat_history.append(result.content)

# print(chat_history)


from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Create Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# Initialize chat history with system message
chat_history = [
    SystemMessage(content="You are a helpful, polite, and knowledgeable assistant.")
]

print("Groq Chatbot 🤖 (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    # Add human message
    chat_history.append(HumanMessage(content=user_input))

    # Invoke model with full history
    result = model.invoke(chat_history)

    # Print AI response
    print("AI:", result.content)

    # Add AI response to history
    chat_history.append(AIMessage(content=result.content))

# Optional: see full structured history
print(chat_history)



