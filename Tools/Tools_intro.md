- a tool is just a function that is packaged in a way the LLM can understand and call when needed.
- the tools are also `Runnables` that can be invoked.
- two types of tools - 1. built in tools 2. custom tools

**1. Built-in Tools**
- these are pre-built and ready to use with minimal setup requirement.

Eg: DuckDuckGo search tool
```
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
response = search_tool.invoke('give me top 10 industry news for today')
print(response)
```

Eg: ShellTool
```
# install this dependency: !pip install langchain_experimental

from langchain_community.tools import ShellTool
shell_tool = ShellTool()
response = shell_tool.invoke('ls')
print(response)
```

**2. Custom Tools**
- some use cases like: u wanna call ur own APIs, encapsulate business logic, interact with ur db, product or application

example: 
1. using @tool decorator to make any custom function as a tool

```
@tool
def my_custom_function(a: int, nums:list):
    '''write the info about ur function here'''
    # write ur business logic


my_custom_function.invoke(2, [32, 12, 89])

print(my_custom_function.name)
print(my_custom_function.description)
print(my_custom_function.args)
```

2. using `StructuredTool` and Pydantic

- in StructuredTool input to the tool follows a structured schema, defined using a Pydantic schema

```
class CustomClass(BaseModel):
    a: int = Field(required=True, description="no of students")
    course_fee: list = Field(required=True, description="Fee of courses they are enrolled in")


def custom_func(a: int, course_fee: list) -> int:
    return a*course_fee

fee_tool = StructuredTool.from_function(
    func=custom_fun,
    name='fee_calculator',
    description='calculate total fee of the class',
    args_schema=CustomClass
)

result = fee_tool.invoke({'a': 4, 'course_fee':[200, 140, 150, 80]})
print(result)

print(fee_tool.name)
print(fee_tool.description)
```

3. using `BaseTool` class
- it is the abstract base class for all tools in langchain. It defines the core structure and interface that nay tool must follow
- all other tool types like `@tool`, `StructuredTool` are built on top of `BaseTool`

example:

```
class CustomClass(BaseModel):
    a: int = Field(requried=True, description="any desc")
    b: int = Field(required=True, description="any other desc")

class MyTool(BaseTool):
    name: str = 'any_tool'
    description: str = 'give the desc'

    args_schema: Type[BaseModel] = MyClass

    def _run(self, a: int, b: int) -> int:
        return a+b

my_tool = MyTool()

response = my_tool.invoke({'a': 4, 'b':7})

print(response)

print(my_tool.name)
print(my_tool.description)
```

**Toolkits**
- all related tools can be packaged together for reusability

example:

```
@tool
def tool_one():
    """tool one"""
    # logic here

@tool
def tool_two():
    """tool two"""
    #logic here

class MyToolkit:
    def get_tools(self):
        return [tool_one, tool_two]

toolkit = MyToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, ": " , tool.description)
```