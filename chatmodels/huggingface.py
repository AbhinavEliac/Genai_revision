from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V4.1-Flash-1017",
#    temperature = 0
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("What is Cricket?")

print(response.content)