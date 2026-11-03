from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = init_chat_model("gpt-4o-mini", temperature = 0.9, max_tokens = 150)

print("Welcome to ChatBot 360-----Type 0 to exit.")

print("Press 1 for Funny AI Agent.")
print("Press 2 for Sad AI Agent.")
print("Press 3 for Angry AI Agent.")

choice = int(input("Enter your mode choice: "))

if choice == 1:
    mode = "You are a Hilarious AI Agent"
elif choice == 2:
    mode = "You are a Sad AI Agent"
elif choice == 3:
    mode = "You are an Angry AI Agent"


messages = [
    SystemMessage(content = mode)
]

while True:    

    prompt = input("You : ")

    messages.append(HumanMessage(content = prompt))

    if prompt == "0":
        print("AI : ", "Thank you for using ChatBot 360")
        break
    else:
        response = model.invoke(messages)
        reply = "AI : " + response.content
        print(reply)
        messages.append(AIMessage(content = reply))
        print("")

print(messages)