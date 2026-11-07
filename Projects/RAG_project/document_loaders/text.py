from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

filepath = r"C:\DS_and_AI\Projects_and_Tutorials\Tutorials\Gen_ai\Projects\RAG_project\covariance_vs_correlation.txt"

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10
)

data = TextLoader(filepath, encoding="utf-8")

docs = data.load()

chunks = splitter.split_documents(docs)

for chunk in chunks:

    print(chunk.page_content)

    print()
    print()
    print()

print(len(chunks))