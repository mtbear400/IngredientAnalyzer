import streamlit as st
import openai
import os
import re
import json

def format_for_markdown_lists(response):
    # Find all markdown lists in the response
    return re.sub(r"(\s|^)- (.+?)(\s|$)", r"\1\n- \2\n\3", response)


# Configure Secrets
def configure_secrets():
  openai.api_key = os.environ.get("OPENAI_API_KEY")
