from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"

)

model = ChatHuggingFace(llm=llm)

# parser = PydanticOutputParser()

class Person(BaseModel):

    name: str = Field(description="the name of the person")
    age: int = Field(gt=18, description="the age of the person")
    city: str = Field(description="the city where the person lives")

parser = pydanticOutputParser = JsonOutputParser(pydantic_object=Person) 

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person\n{format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place': 'indian'})

print(result)

# prompt = template.invoke({'place': 'Pakistani'})

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
