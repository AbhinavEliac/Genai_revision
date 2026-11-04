from langchain_community.document_loaders import TextLoader, PyPDFLoader

filepath = r"C:\DS_and_AI\Projects_and_Tutorials\Tutorials\Gen_ai\Projects\RAG_project\covariance_vs_correlation.txt"

data = TextLoader(filepath, encoding="utf-8")

docs = data.load()

print(docs[0])