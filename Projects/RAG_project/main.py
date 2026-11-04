from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

filepath = r"C:\DS_and_AI\Projects_and_Tutorials\Tutorials\Gen_ai\Projects\RAG_project\deep_learning_and_transformers.pdf"

data = PyPDFLoader(filepath)
docs = data.load()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Helpful Text Expert AI Assistant that Summarizes Text from PDF"),
        ("human", "{data}")
    ]
)

model = init_chat_model(
    "gpt-4o-mini", 
    temperature = 0
)

prompt = prompt_template.format_messages(data = docs[0].page_content)

response = model.invoke(prompt).content

print(response)