def chatbot():
    print("Hi, I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input :
            print("Bot: Hello! How can I help you?")
        elif 'name' in user_input:
            print("Bot: I'm a Python Chatbot.")
        elif 'how are you' in user_input:
            print("Bot: I'm doing great, thanks for asking!")
        elif 'bye' in user_input:
            print("Bot: Bye! Have a great day!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
