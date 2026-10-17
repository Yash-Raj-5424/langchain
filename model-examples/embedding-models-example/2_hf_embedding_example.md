an example how to use any huggingface's embedding model

```
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "text1 for this doc",
    "sample text for the doc",
    "sample text2 for this document"

]

vector = embedding.embed_documents(documents)

print(str(vector))
```