- 6 components of langchain =>  models, prompts, chains, memory, indexes, agents

1. **Models** are the core interface through which you interact with AI models
- langchain generally interacts with two types of models => 1. language models (LLMs -> that take text input and give text output) 2. embedding models (models that take text input and give vector output -> semantic search is an example)

2. **Prompts** - the input to the LLMs
- types of prompts: reusable prompts, role-based prompts, few shot prompting (show some example of input n output and then ask the query)

3. **Chains** - we can build pipelines using chains. we can build parallel or conditional chains

4. **Indexes** - it connects the application to external knowledge such as websites or databases. components of indexes are: doc loader, text splitter, vector store, retrievers.
- we can connect our LLM to an external knowledge source 

5. **Memory** - LLM API calls are stateless so one call doesn't have the context of the previous call. 
- **types of memory:**
- ConversationBufferMemory: Stores a transcript of recent messages. Great for short chats but can use large context quickly.

- ConversationBufferWindowMemory: Only keeps the last N interactions to avoid excessive token usage.

- Summarizer-Based Memory: Periodically summarizes older chat segments to keep a condensed memory footprint.

- Custom Memory: For advanced use cases, you can store specialized state (e.g., the user's preferences or key facts about them) in a custom memory classversation buffer window memory, summarizer based memory, custom memory

6. **Agents** -  normal LLMs have NLU (natural language understanding and text generation capability). but AI agents have the reasoning capability and tool access. it can use chain of thoughts to perform any sort of task/action.