- just an example code (I didn't have OpenAI API key so just raw text in md file)

```
from langchain_openai import OpenAI
from dotenv import load_dotenv  

load_dotenv()   # loads the API keys from env file (u store ur API keys there)

llm = OpenAI(model='gpt-3.5-turbo-instruct')    # u can give any model name u wish

result = llm.invoke("Tell me the capital of Lebanon")
print(result)
```