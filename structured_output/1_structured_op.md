- structured output by the LLMs are useful in many tasks like data extraction, database communication and many others.
- there can be two type of models - one that generate structured output by default and the other that don't generate structured output
- the models that generate structured output, we can use `with_structured_output` function to specify the data format in which we want our output
- the models that can't generate structured output - we can use `output parsers` to get our desired output data format

**with_structured_output**
- we have to call `with_structured_output` and specify our data format - `TypedDict`, `Pydantic`, `json_schema`
- **TypedDict** is a way to define a dictionary in python where u specify what keys and values should exist. it tells python what keys are req and what types of values they should have
- it doesn't validate data at runtime (just gives hints for better coding). this is how u use TypedDict for structured output:

```
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """
    <PASS_YOUR_REVIEW_TEXT_HERE>
   """
)

print(result['name'])
```

> `Annotated` adds extra metadata or instructions to a type; `Optional` means a value can be the specified type or None. The field can still be required in the TypedDict unless you explicitly make it non-required. `Literal` restricts a value to a fixed set of allowed values

- the other type is `pydantic` that strictly defines the req data format unlike `TypedDict`. this is how u use it:

```
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """
    <PASS_YOUR_REVIEW_TEXT_HERE>
    """
    )

print(result)
```

> `BaseModel`: Defines a structured data model and provides validation of the returned data. `Field()`: Specifies field descriptions, default values, and other validation rules. `default=None`: Makes a field optional by providing None as its default when no value is supplied. `Literal["pos", "neg"]`: Restricts sentiment to "pos" or "neg"
> we could also convert the result to a dictinory using `result.model_dump()`
> it is better to store the review in a separate text file and read it from there and pass into invoke. this would make the code clean. this is how u'd do it:

```
with open("review.txt", "r", encoding="utf-8") as file:
    review_text = file.read()

# and now pass `review_text` in the `model.invoke()`
```

- the other type is `json_schema`. this is how u use it:

```
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# schema
json_schema = {
    <PASS_YOUR_SCHEMA_HERE>
    }


structured_model = model.with_structured_output(json_schema)

#load review from review.txt
with open("review.txt", "r", encoding="utf-8") as f:
    review_text = f.read()

# pass the review_text into the model
result = structured_model.invoke(review_text)

print(result)
```

> here too, the `json_schema` can be stored in a separate json format file and loaded into this file as below:

```
with open("review_schema.json", "r", encoding="utf-8") as f:
    json_schema = json.load(f)

structured_model = model.with_structured_output(json_schema)
```
