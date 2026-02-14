from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema



load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"

)

model = ChatHuggingFace(llm=llm)

Schema = [
    ResponseSchema(name="fact_1", description="the first fact about the topic"),
    ResponseSchema(name="fact_2", description="the second fact about the topic"),
    ResponseSchema(name="fact_3", description="the third fact about the topic"),
    ResponseSchema(name="fact_4", description="the fourth fact about the topic"),
    ResponseSchema(name="fact_5", description="the fifth fact about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(Schema)

template = PromptTemplate(
    template=' Give me 5 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt = template.invoke({'topic': 'black holes'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)