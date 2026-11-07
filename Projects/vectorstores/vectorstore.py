from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

filepath = r"C:\DS_and_AI\Projects_and_Tutorials\Tutorials\Gen_ai\Projects\RAG_project\deep_learning_and_transformers.pdf"

loader = PyPDFLoader(filepath)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)

chunks = splitter.split_documents(docs)

# for chunk in chunks:

#     print(chunk)
#     print()
#     print()

# print(len(chunks))

embedding_model = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents = docs,
    embedding = embedding_model,
    persist_directory = "chroma-db"
)

result = vectorstore.similarity_search("What is used for deep learning?", k = 5)

for r in result:
    print()
    print(r)

retriever = vectorstore.as_retriever()

docs = retriever.invoke("Explain Deep Learning")

for d in docs:
    print()
    print(d.page_content)