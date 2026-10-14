- LangChain is an open-source framework for developing applications powered by large language models
- say we wanna build a document QnA platform. this would be a high level design of this system:

```
user query => semantic search on doc => pages of the doc + user query --> system query => brain => final output
```

- we first create a vector embedding of the document and the query. and then we find the similarity bw the query vector and the document vector
- this is how the flow looks like:
> pdf upload => AWS S3 ==doc loader=> pdf ==text splitter=> pg1, pg2... pg_n => embedding1, emb2.... => store them in db <= semantic search <= query embedding <= user query. now we use user query and doc pages to form system query and it is sent to the system brain that gives final output. [ this brain would be an LLM ]

**benefits of langchain**
- concept of chains (output of one component becomes the input of other component)
- model agnostic development
- complete ecosystem
- memory and state handling

**what can we build using langchain**
- conversational chatbot
- AI knowledge assistants
- AI agents
- workflow automation
- summarization/research helpers

**alternatives of langchain**
- Llamaindex
- haystack