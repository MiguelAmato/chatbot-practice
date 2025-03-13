""" Main logic for the ChatBot
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

class ChatBot:
    
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = []

    def call_llm(
        self,
        message:str,
        model:str="gpt-4o-mini",
        temperature:float=0.3
        ) -> str:
        """Main call to the OpenAI API

        Args:
            message (str): User message.
            model (str, optional): Set the model on the OpenAI catalog. Defaults to "gpt-4o-mini".
            temperature (float, optional): Set the model temperature. Defaults to 0.3.

        Returns:
            Response: The return of the API call
        """
        
        self.messages.append({"role": "user", "content": message})
        
        response = self.client.chat.completions.create(
            model=model,
            messages=self.messages,
            temperature=temperature,
        )
        
        bot_response = response.choices[0].message.content
        
        self.messages.append({"role": "assistant", "content": bot_response})
        
        return bot_response