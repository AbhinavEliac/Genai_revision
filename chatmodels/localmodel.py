from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs = dict(
        max_new_tokens = 512,
        do_sample = False,
        repetition_penalty = 1.03
    )
)

model = ChatHuggingFace(llm = llm)

prompt = "Hello Who Are you?"

response = model.invoke(prompt).content

print(response)