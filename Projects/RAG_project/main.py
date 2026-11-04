from dotenv import load_dotenv

from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "gpt-4o-mini", 
    temperature = 0
)

prompt = "What is RAG?"

response = model.invoke(prompt).content

print(response)