import os

# Environment variables are a secure way to store sensitive information
# You should set these in your virtual environment or your system's environment settings

# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# EDAMAM_API_KEY = os.getenv('EDAMAM_API_KEY')
# EDAMAM_APP_ID = os.getenv('EDAMAM_APP_ID')

# Hardcoded for dev but DELETE before pushing to git




# OPENAI_API_KEY = ""
# EDAMAM_API_KEY = os.getenv('EDAMAM_API_KEY')
# EDAMAM_APP_ID = os.getenv('EDAMAM_APP_ID')





# def get_openai_key():
#     """
#     Fetches the OpenAI API key from environment variables.
#     Handles the case when the key is not found.
#     """
#     try:
        
#         return os.environ["OPENAI_API_KEY"]
#     except KeyError:
#         raise Exception("Couldn't find the OpenAI API key in environment variables. Please set it and try again.")