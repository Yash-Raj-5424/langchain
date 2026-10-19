- output parsers are used for those models that can't generate structured output. the output parser helps to convert the raw response to structured format like JSON, CSV etc.
- some of the output parsers: strOutputParser, JSONOutputParser, StructuredOutputParser, PydanticOutputParser

**StrOutputParser** - parse the output and return it as a plain string. this is how u use it:

```
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# 1st prompt -> generate a detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on: \n{text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'the black holes'})
detailed_report = model.invoke(prompt1)

# now parse it
parsed_report = parser.invoke(detailed_report.content)

prompt2 = template2.invoke({'text':detailed_report.content})
summary_response = model.invoke(prompt2)

# parse the summary
parsed_summary = parser.invoke(summary_response)

print(parsed_summary)
```

> here, invoke is called multiple times so, same stuff - we could form a chain and invoke the chain directly instead of creating two prompts separately. below is how u'd do it:

```
chain = template1 | model | parser | template2 | model | parser
response = chain.invoke({'topic': 'the black holes'})
```

- **JSONOutputParser**

```
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# response = model.invoke(prompt)
# structured_response = parser.parse(response.content)

# print(structured_response)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})

print(result)
```
- the JSONOutputParser doesn't enforce a schema

**StructuredOutputParser** - helps extract structured JSON from response based on predefined field schemas. 
- it works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows a structured format
- this is how we use it:

```
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='brief_history', description='A brief history about the topic'),
    ResponseSchema(name='current_trends', description='Current trends of the topic'),
    ResponseSchema(name='future_scopes', description='Future scopes of the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give informations about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'Artificial Intelligence'})

print(result)
```
- it doesn't enforce schema validation. so we use PydanticOutputParser when schema validation is needed strictly

**PydanticOutputParser** - enforces schema validation strictly using BaseModel
- this is how u use it:

```
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'place':'Latin American'})

print(final_result)
```