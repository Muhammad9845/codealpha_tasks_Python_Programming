def simple_chatbot():
    """
    Simple Rule-Based Chatbot for CodeAlpha Internship
    """
    print("=" * 50)
    print("WELCOME TO CODEALPHA CHATBOT")
    print("=" * 50)
    print("You can type: hello, name, how are you, help, bye")
    print("Type 'bye' to exit the chat\n")

    # Predefined responses
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! Nice to meet you!",
        "how are you": "I'm doing great, thank you! How about you?",
        "what is your name": "I'm CodeAlpha Bot, your Python programming assistant!",
        "name": "I'm CodeAlpha Bot, created for Python internship tasks!",
        "what can you do": "I can chat with you and help you learn Python programming!",
        "codealpha": "CodeAlpha is a software company offering internship programs!",
        "internship": "CodeAlpha offers internships in Python, Data Analytics, and more!",
        "bye": "Goodbye! Thanks for chatting. Good luck with your internship!",
        "thank you": "You're welcome! Happy to help!",
        "help": "I understand these phrases: hello, hi, how are you, name, codealpha, internship, help, bye, thank you"
    }

    chat_count = 0

    while True:
        user_input = input("YOU: ").lower().strip()
        chat_count += 1

        # Check for exit condition
        if user_input in ['bye', 'exit', 'quit', 'goodbye']:
            print(f"BOT: {responses['bye']}")
            break

        # Find matching response
        response_found = False
        for key in responses:
            if key in user_input:
                print(f"BOT: {responses[key]}")
                response_found = True
                break

        # Default response if no match found
        if not response_found:
            print("BOT: I'm sorry, I didn't understand that. Type 'help' to see what I can understand.")

    # Chat summary
    print(f"\nCHAT SUMMARY:")
    print(f"- Total messages exchanged: {chat_count}")
    print(f"- Chatbot session ended.")
    print("=" * 50)


def chatbot_info():
    """
    Display information about the chatbot
    """
    print("\nCHATBOT INFORMATION:")
    print("- Built for CodeAlpha Python Programming Internship")
    print("- Task: Basic Chatbot (Task 4)")
    print("- Uses simple rule-based responses")
    print("- Demonstrates: functions, loops, conditionals, dictionaries")


if __name__ == "__main__":
    chatbot_info()
    simple_chatbot()