import re

responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm here to help!",
    "bye": "Goodbye! Have a great day.",
    "name": "I'm CodSoft's AI chatbot!",
    "weather": "I can't predict the weather, but checking an online forecast might help!",
    "age": "I don't age, but I keep learning!"
}

def chatbot():
    print("Simple Chatbot: Type 'bye' to exit")
    
    while True:
        user_input = input("You: ").lower()
        matched_response = None

        for pattern, response in responses.items():
            if re.search(pattern, user_input):
                matched_response = response
                break

        if matched_response:
            print(f"Bot: {matched_response}")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()