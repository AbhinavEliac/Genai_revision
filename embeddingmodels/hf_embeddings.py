from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name = "BAAI/bge-small-en-v1.5",

)

texts = [
    "What is the Capital of France?",
    "What is the Capital of Sextan?",
    "What is the Capital of India?"
    ]
vectors = embeddings.embed_documents(texts)

print(vectors)