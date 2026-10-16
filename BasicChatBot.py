print("Basic Chatbot")
while True:
    prompt=input("You :")
    pt=prompt.lower()
    if pt=='hello':
        print("ChatBot : hi!\n")
    elif pt=='how are you':
        print("ChatBot :I'm Fine Thanks!\n")
    elif pt=='tell me a joke':
        print("ChatBot :Why do programmers prefer dark mode? because light attracts bugs!\n")
    elif pt=='help':
        print("ChatBot :Sure! ask me questions and i will try to help you\n")
    elif pt=='thank you':
        print("ChatBot :You're Welcome\n")
    elif pt=='bye':
        print("Goodbye!")
        break
