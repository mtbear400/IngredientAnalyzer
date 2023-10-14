import requests
from typing import Dict, Any
# Assuming edamam_call.py is in a directory named 'utilities'
from edamam_call import get_ingredients
import openai  # Make sure the openai library is installed

def extract_and_get_ingredients(user_input: str, openai_api_key: str) -> str:
    """
    Extracts the product name from the user's input via a GPT call, and retrieves product 
    information using the Edamam API.

    :param user_input: Text input from the user.
    :param openai_api_key: API key for authenticated access to OpenAI's GPT.
    :return: A string containing product details or an error message.
    """

    # GPT-3 call to extract product name
    prompt = f"Please extract the product name from this prompt: '{user_input}'. Your response should only be the name of the product."
    
    try:
        openai.api_key = openai_api_key  # Set the API key here
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # gpt-4 isn't available, use gpt-3.5-turbo or another available model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        product_name = response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        return f"Error during GPT call: {str(e)}"

    # Fetching and returning product details
    product_details = get_ingredients(product_name)
    return product_details
