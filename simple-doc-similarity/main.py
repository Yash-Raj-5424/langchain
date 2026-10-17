from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding_model = OpenAIEmbeddings(model = 'text-embedding-3-large', dimension=300)

documents = [
    "Bananas are berries, but strawberries are not.",
    "Octopuses have three hearts.",
    "A group of flamingos is called a flamboyance.",
    "The Moon has moonquakes.",
    "Some turtles can breathe through their rear ends."
]


query = "what are berries?"

doc_embeddings = embedding_model.embed_documents(documents)
query_embeddings = embedding_model.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print('similarity score is: ' ,score)
