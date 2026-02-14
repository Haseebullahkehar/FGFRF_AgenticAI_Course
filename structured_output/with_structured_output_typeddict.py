# # from langchain_groq import ChatGroq
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from typing import TypedDict

# load_dotenv()

# model = ChatGoogleGenerativeAI()

# # schema 
# class Review(TypedDict):
#     summary: str
#     sentiment: str 

# structured_model = model.with_structured_output(Review)


# # simple flow 

# result = structured_model.invoke("This software has completely streamlined our project scheduling process. " 
# "The timeline tracking and resource allocation tools make it much easier to stay on deadline")

# print(result)
# print(result['summary'])
# print(result['sentiment'])


# from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatGoogleGenerativeAI()

# schema 
class Review(TypedDict):
    key_themese: Annotated[list[str], "The main themes or topics mentioned in the review"]
    summary: Annotated[str, "A concise summary of the review"]
    sentiment: Annotated[str, "The overall sentiment of the review, e.g., positive, negative, neutral"]
    pros: Annotated[Optional[list[str]], "A list of pros mentioned in the review, if any"]
    cons: Annotated[Optional[list[str]], "A list of cons mentioned in the review, if any"]

structured_model = model.with_structured_output(Review)


# simple flow 

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

**Pros:**
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

**Cons:**
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors

""")

print(result)
print(result['summary'])
print(result['sentiment'])


