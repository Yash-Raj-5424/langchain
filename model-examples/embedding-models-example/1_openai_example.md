- here is an example of using openAI's paid chat model for both embedding a query and embedding a doc
>NOTE: u must have api key in an env file

**embedding a query**
```
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of mauritania")

print(str(result))
```

**embedding a doc**
```
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32) # u can choose wtever dimension u want

documents = [
    "sample text for document",
    "sample text2 for doc",
    "sample text3 for the doc"
]

result = embedding.embed_documents(documents)

print(str(result))
```