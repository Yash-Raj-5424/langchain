- two types of prompt: static prompt (user types completely), dynamic prompt(there's a template with placeholders, which user fills as desired)

**static prompt example:**
```
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

user_prompt = input('Enter your prompt: ')
result = model.invoke(user_prompt)

print(f'Model result: {result}')

```

**dynamic prompt example:**
> say you have a prompt template and three placeholders {paper_name}, {response_style} and {response_length}. this is how we use dynamic prompts:

```
# create a template, fill the placeholders to get the prompt, get the result by invoking model with prompt

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()


# prepare a prompt template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_name}" with the following specifications:
Explanation Style: {response_style}
Explanation Length: {response_length}
1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
   - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_name', 'response_style', 'response_legth']
)

# we can use validate input as input_variables=['a', 'b', validate_template=True] => this will ensure u provide proper inputs

# take placeholder inputs from the user
paper_name = input('Enter paper name: ')
response_type = input('Enter response type u want: ')
response_length = input('Enter response length u want: ')

# now fill the placeholders in the template
prompt = template.invoke(
    {
        'paper_name':paper_name,
        'response_style':response_style,
        'response_length':response_length
    }
)

result = model.invoke(prompt)   # send prompt to model
print(response)

```

- **Prompt Template** is a structured way to create prompts dynamically by inserting variables into a predefined template. it allows u to fill the placeholders at runtime. Prompt Templates provide u default validation for inputs, these are reusable and well suited for Langchain ecosystem so it's preferred over fstrings

> it would be better to keep prompt template in other file and load it from there in our main file. this is how it would work:

```
# create a generator file that'll generate a json for ur prompt template

# below is the code:

from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = """
        <ENTER_YOUR_TEMPLATE>
    """
)

template.save('<FILENAME.json>')    # this will create a json file for ur template that u can load in ur main file

# to load the prompt in the main file: from langchain_core.prompts import load_prompts and then template = laod_prompt(<FILENAME.json>) rest all code will be the same
```

- we're calling invoke twice - once for creating prompt and then for invoking model. here we can use **chain** to invoke only once. this is how to do it:

```
# all above code stays same till template = laod_prompt(xyz)

chain = template | model
response = chain.invoke(
    {
        'paper_name':paper_name,
        'response_style':response_style,
        'response_length':response_length
    }
)

print(response.content)
```

