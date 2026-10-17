
```
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
res = model.invoke("tell me capital of lebanon")
print(res.content)
```

> chat models give u some metadata along with the content (the res in not in plaintext so u extract content)