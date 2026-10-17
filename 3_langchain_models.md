**models** - designed to facilitate interaction with various language models and embedding models. it abstracts the complexity of working directly with different LLMs, chat models and embedding models providing a uniform interface to communicate with them. this makes it easier to build application that rely on AI-generated text, text embeddings for similarity search and retrieval augemented generation (RAG).

```
models -> [language models -> [LLMs, Chat Modles], [embedding models]]
```

**Language Models** - Ai systems desinged to process, generate and understand natural language text
- **LLMs**: general purpose models that are used for raw text generation. they take a string/plain text as input and return a string/plain text. these are traditionally older models and are not used much now
- **Chat Models**: specialized for conversational tasks. they take a seq of msg as input and return chat msg as output (as opposed to using plain text). these are traditionally newer models and used more in comparison to LLMs