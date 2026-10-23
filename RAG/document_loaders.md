- document loaders are used to load data from various sources into a standardized format (Document objects) which can then be used for chunking, embedding, retrieval and generation
- the result of loader is a list of `Document`

**Document**
```
Document(
    page_content="actual text content here",
    metadata={"name":"filename.pdf", etc...}
)
```

**1. TextLoader**
- reads plain text files and converts them to Document obj. this is how u use it:

```
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
```

**PyPDFLoader**
- used to load content from PDF files and convert each page to Document. this is how u use it:

```
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)
```

**DirectoryLoader**
- used to load multiple docs from a directory
- this is how u use it:

```
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
```

**lazy_load()**
- gives u a `generator` of Document objects and they're fetched one at a time as needed

**WebBaseLoader**
- used to load and extract text content from web page URLs
- it uses `BeautifulSoup` to parse HTML and extract visible content
- good for static pages
- u can also pass a list of urls and it'll give u a `Document` for each url

this is how u use it:

```
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))
```

**CSVLoader**
- loads CSV files into LangChain Document objects - one per row by default

this is how u use it:

```
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])
```