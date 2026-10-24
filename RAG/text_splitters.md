- text splitter is the process of breaking larger chunks of text into smaller manageable pieces(chunks) that an LLM can handle effectively
- text splitters helps in embeddings, semantic search, summarization
- four types text splitters are - length based, text structure based, document structure based, semantic meaning based

**Length based text splitting**
- it strictly splits based on length. so, often the chunks end up having no meaning as they abruptly get split based on length
- u get a list of strings after splitting
- the chunks can be based on the no of chars or tokens. this is how u use it:

```
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)
```

**Text structure based text splitting**
- recursive character text splitting - we predefine some separators as \n\n, \n, '_', ""

this is how u use it:

```
from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
<ENTER_TEXT_HERE>
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)
```

**Document structure based**
- it is used for splitting other type of documents such as markdown, code files (u should specify which language the code is in. Eg: PYTHON, GO...) etc.
- we use recursive character text splitting but separators are some other types. this is how u use it:

1. markdown splitting

```
from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """
<ENTER_MARKDOWN_TEXT_HERE>
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])
```

2. Code splitting. here we hv an example of a python code.

```
from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """
<ENTER_PYTHON_CODE_HERE>
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[1])
```

**Semantic meaning based splitter**
- use a sliding window approach and keeps comparing cosine similarity of sentences and splits when the similarity score becomes low

this is how u use it:

```
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
<ENTER_TEXT_HERE>
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)


```