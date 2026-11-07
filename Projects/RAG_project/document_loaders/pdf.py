from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

load_dotenv()

filepath = r"C:\DS_and_AI\Projects_and_Tutorials\Tutorials\Gen_ai\Projects\RAG_project\deep_learning_and_transformers.pdf"

data = PyPDFLoader(filepath)

docs = data.load()

splitter = TokenTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)

for chunk in chunks:

    print(chunk.page_content)
    print()
    print()
    print()

print(len(chunks))