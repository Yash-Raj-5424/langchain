- a Retriever is a component in Langchain that fetches relevant documents from a data source in response to a user's query

basic flow is like this
```
user query -> [retriever searchs the relevant data sources] -> a list of Document objects
```

- there are multiple retrievers for diff use cases
- the retievers are `Runnables` so u can do everything that u do with Runnables
- types of retrievers - 1. Data source based (wikipedia retriever, vector store retrievers, Arxiv retriever etc.) 2. Search strategy based retrievers (MMR, multi-query, contextual etc.)

**Wikipedia Retriever**
- it refers Wikipedia API for fetching the results. this is how u use it: 

```

```

**Vector Store Retriever**
- it allows to search and fetch docs from a vecstore based on semantic similarity using vec embeddings
- this is how it works: u store ur docs in vecstore -> each doc is converted to a dense vector using an embedding model -> when the user enters a query, the query is turned to vector then retriever compares the query vector with the stored vectors and retrieves the `top-k` most similar vectors.

this is how u use it:

```

```


**Maximal Marginal Relevance (MMR)**
- how can we pick results that are not  only relevant to the query but also different from each other ?
- it reduces redundancy in the retrieved results while maintaining high relevance to the query
- in regular similarity search u may get docs that are all very similar, repeating info, lacking diverse perspective but MMR retriever avoid that by picking most relevant doc first then picking the next relevant and least similar to the already selected one and so on..
- this helps in RAG pipeline where u want ur context window to contain diverse but still relevant info especially when docs are semantically overlapping
- this is how u use it:

```

```

**Mutli-Query Retriever**
- sometimes a single query might not capture all the ways info is phrased in ur docs. eg: how to stay healthy (food ? exercise ? etc. ?)
- this is how it works:

```
query -> LLM -> multiple queries -> perform retrieval for each sub-query -> combine and deduplicate the result
```

- this is how u use it:

```

```

**Contextual Compression Retriever**
- an advanced retriever taht improves the retrieval quality by compressing the docs after retrieval - keeping on ly the relevant content base on the users query
- this is what it does - A `Base Retriever` retrieves `N` docs then a compressor (an LLM) is applied to each doc that keeps only relevant parts of the doc.
- use it when ur docs are long and contain mixed info or u want to reduce cnotext length for LLMs or u need to improve ans accuracy in ur RAG pipeline.

this is how it works:

```

```

