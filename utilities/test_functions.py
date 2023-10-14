from functions import extract_and_get_ingredients  # adjust the import according to your project structure
from settings import OPENAI_API_KEY
# The OpenAI API Key should be stored securely, or use environment variables to keep them out of your codebase.


def main():
    # Simulate a user message
    user_message = "I'm looking to buy Cocoa Puffs."
    
    # Extract product info and get ingredients
    product_info = extract_and_get_ingredients(user_message, OPENAI_API_KEY)
    
    # Print the result
    print(product_info)

if __name__ == "__main__":
    main()
