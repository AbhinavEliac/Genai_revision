from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

filepath = r"C:\DS_and_AI\Projects_and_Tutorials\Tutorials\Gen_ai\Projects\RAG_project\deep_learning_and_transformers.pdf"

data = PyPDFLoader(filepath)

docs = data.load()

print(len(docs))