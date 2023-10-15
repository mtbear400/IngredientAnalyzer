import streamlit as st
import openai
import os
import re
import json

# to use, first activate python venv. 
# in terminal at this directory, run pip install -r requirements.txt
# Run this main.py file to get streamlit working

from utilities.gpt_call import GPTSession
from utilities.message_manager import MessageManager
from utilities.functions import function_definitions  # This assumes functions.py and functions_definitions.py are merged or handled appropriately.
from utilities.user_input_manager import UserInputManager

def main():
    # Initialize components
    message_manager = MessageManager()
    user_input_manager = UserInputManager(message_manager)
    gpt_session = GPTSession(model="gpt-4", message_manager=message_manager, function_definitions=function_definitions)

    # Main loop for chat
    while True:
        # Get and process user input
        user_input, should_continue = user_input_manager.process_input()
        if should_continue:
            continue

        if user_input is None:  # This could happen if there's an input-related command or mode change
            continue

        # Add user message to the message manager
        message_manager.add_message({"role": "user", "content": user_input})

        # Make GPT call and handle functions
        response_text, function_name, function_args = gpt_session.call_to_gpt()

        # Here, you'd have additional logic to handle the response, possibly calling specific functions
        # based on function_name and function_args, or just displaying the response_text to the user.

        # If you're planning to end the session after a certain command, you'd check for that here.

if __name__ == "__main__":
    main()
