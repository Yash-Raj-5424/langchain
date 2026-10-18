let's see how we make a simple chatbot by taking prompt from the user

```
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

while True:
    user_input = input('You: ') # get the user query

    if user_input == 'exit':
        break

    response = model.invoke(user_input) # get the response from the model

    print("AI: ",response.content)
```

> here the problem is that the model doesn't have the context of the messages. this means if u gave hi my name is jack -> model: hi jack how can i help you -> u then ask what is my name -> model doesn't know even though u told it in prev msg as it doesn't have context of the prev msg. so we need some way to store the context of these msgs. say we create a list and store both the user msg and model response in that list and u ask the model for response by passing the list while invoking the model. this is how u do it:

```
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []   # this list will contain the context of the chat

while True:
    user_input = input('You: ')
    
    chat_history.append(user_input) # append user query to the history

    if user_input == 'exit':
        break
    
    response = model.invoke(chat_history) # pass the whole context in the prompt

    chat_history.append(response)   # append the response in the context

    print("AI: ",response.content)

print(f'Chat History:\n{chat_history}')
```

> but here, one problem is that the list contains all the values as it is. we don't konw which one is the user query and which one is the model response. there must be a way to store the responses of model, the user query properly in the list. For this, Langchain provides **three types of messages - SystemMessage, HumanMessage and AIMessage. so we store the context in the list by properly labelling them as one of these three. this way, the model will have proper context of the chat and will know which one is which type of msg. below is how u do it:

```
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]   # SystemMessage is given at the start

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))

    print("AI: ",response.content)

print(f'Chat History:\n{chat_history}')
```

- here we discussed about list of static messages. how do we use a prompt template for the list of messages ? For that, Langchain provides `ChatPromptTemplate`. this is how u use it:

```
from langchain_core.prompt import ChatPromptTemplate, ChatOpenAI
from dotenv import load_dotenv

model = ChatOpenAI()

# prepare a chat template with placeholders
chat_template = ChatPromptTemplate([
    ('system', 'Your are a {domain} expert'),
    ('human', 'Tell me about {topic}')
])

# fill the placeholders to prepare a prompt
prompt = chat_template.invoke(
    {
        'domain': 'databases',
        'topic': 'MVCC and autovacuum in postgres'
    }
)

# pass the prompt to the model to get the response
response = model.invoke(prompt)

print(response)

```

- consider a scenario where a user did some chats and later some other day came to chat again. how would the model keep the context of the previous messages. for this, Langchain provides `MessagesPlaceholder` from `langchain_core.prompts`. this helps to store and retreive chat history. this is how u use it:

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# prepare a template
chat_template = ChatPromptTemplate([
    ('system', 'Yout are a helful AI assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())  # load the context from the file

# prepare a prompt by filling placeholders
prompt = chat_template.invoke(
    {
        'chat_history': chat_history,
        'query': 'what is the status of my refund'
    }
)

# get the response by passing the prompt
response = model.invoke(prompt)

print(response.content)
```