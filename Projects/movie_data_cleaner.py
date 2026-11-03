from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = init_chat_model("gpt-4o-mini", temperature = 0)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a Professional Movie Extractor Agent.

            Your Task: Extract useful structured information from a Movie Paragraph and present it in a clean readable format.

            Rules:

            - do not add any explanations.
            - do not add any commentary. 
            - Follow the Exact Format.
            - If Information is Missing : Write Null.
            - Keep Summary Short (2 - 3 lines max).
            - Do not guess unknown facts.

            Output Format:

            Title:- 
            Director:- 
            Release Date:- 
            Genre:- 
            Plot:- 
            Theme:- 
            Setting/location:- 
            Lead Actors:- 
            Plot Summary:- 

            """
        ),
        (
            "human",
            """
            Extract information from this movie paragraph.

            Movie Paragraph: {paragraph}
            """
        )
    ]
)

para = input("Give me the Movie Paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph" : para}
)

response = model.invoke(final_prompt)

print(response.content)