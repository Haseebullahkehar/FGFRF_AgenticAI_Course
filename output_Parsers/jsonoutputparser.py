from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"

)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    # template=' Give me the name, age and city of a fictional person \n {format_instructions}',
    # input_variables=[],
    template=' Give me 5 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt) 

# final_result = parser.parse(result.content)

chain = template | model | parser

result = chain.invoke({'topic':'black holes'})

# print(final_result['name'])

# print(type(final_result))
print(result)



# print(prompt)

