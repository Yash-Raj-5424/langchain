- LLMs are giant transformer based neural network architecture. they store their knowledge in the parameters - weights & biases (parametric knowledge)
- we get the responses from them by prompting
- **fine tuning** is training a pre-trained model on a small domain specific dataset -- [supervised/unsupervised(continued pretraining)]

**In context learning**
- model learns to solve a task purely by seeing examples in the prompt - without updating its weight. it's an emergent property of the LLMs. (few shot prompting)

**RAG is a way to make a language model smarter by giving it extra info at the time u ask ur question**

```
query + context -> prompt -> LLM -> response
```

> RAG = info retrieval + text generation

1. **indexing** - preparing an external knowledge base
- document ingestion (load source knowledge into memory), text chunking (break into small, semantically meaningful chunk), embedding (convert each chunk into dense vector that captures meaning), store in a vector store/db (chunks + metadata is stored)

2. **retrieval** - finding the most relevant chunk in the knowledge base based on user query
- generate an embedding of the query and search the closest embedding vector and then rank the results and fetch the top results

3. **augmentation** - creating a prompt from query+context
- prepare a prompt from the context and the user query that'll be sent to the LLM

4. **generation** - generating the response by text generation and in-context learning + its parametric knowledge

