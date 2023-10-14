import streamlit as st
import openai
import os
import re
import json

# to use, first activate python venv. 
# in terminal at this directory, run pip install -r requirements.txt
# Run this main.py file to get streamlit working


def format_for_markdown_lists(response):
    # Find all markdown lists in the response
    return re.sub(r"(\s|^)- (.+?)(\s|$)", r"\1\n- \2\n\3", response)


# Configure Secrets
def configure_secrets():
  openai.api_key = os.environ.get("OPENAI_API_KEY")
