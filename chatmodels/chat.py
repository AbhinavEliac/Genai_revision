from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("gpt-4o-mini", temperature = 0.9, max_tokens = 150)

response = model.invoke("What is Cricket?")

print(response.content)