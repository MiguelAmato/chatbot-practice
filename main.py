""" Chatbot Command Line Interface script. """

import argparse

from src.chatbot.controller import ChatBot

def main() :
    
    bot = ChatBot()
    
    print("\n ChatBot CLI - Escribe 'salir' para terminar\n")
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Hasta luego!")
            break
        
        response = bot.call_llm(user_input)
        
        print(f"Bot: {response}\n")
        
if __name__ == "__main__":
    main()