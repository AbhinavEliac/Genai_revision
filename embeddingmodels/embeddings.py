from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    dimensions = 64
)

texts = [
    "What is the Capital of France?",
    "What is the Capital of Sextan?",
    "What is the Capital of India?"
    ]
vectors = embeddings.embed_documents(texts)

print(vectors)