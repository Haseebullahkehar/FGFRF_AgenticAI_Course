from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimension=32)

result = embeddings.embed_query("What is the capital of Pakistan?")

print(str(result))

# conda create -n lang_env python==3.12



