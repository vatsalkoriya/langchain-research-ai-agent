from agent import ask_agent

print("🤖 AI Research Agent")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    print("\nAgent:", ask_agent(question))
    print()