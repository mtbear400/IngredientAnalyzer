# to use in terminal: streamlit run FILEPATH 

import streamlit as st
import openai
from functions import extract_and_get_ingredients  # Adjust this import statement as necessary.
import os

st.title("Royal Taster")

# Set OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

if "openai_model" not in st.session_state: 
    st.session_state["openai_model"] = "gpt-4"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What food should I check out?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Extract product info and get ingredients
    product_string = extract_and_get_ingredients(prompt, OPENAI_API_KEY)

    # Parse the product_string for display
    product_details, image_url = product_string.rsplit("\nImage: ", 1)
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display the product details
    with st.chat_message("assistant"):
        st.markdown(product_details)
        st.image(image_url)  # Uncomment this to display the image

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        initial_prompt = f"You are a food expert who specializes in longevity wellness. Our grocery stores are full of processed foods with long ingredients lists that the average consumer doesn't understand. You will be asked about specific food items and you will be given their ingredients. Your job is to identify unnatural and potentially harmful ingredients in a product as if the person asking you wants to cut out all the processed junk in their foods. For example, if you are familiar with ICE drinks called Sparkling Ice 'Flavored Sparkling Water', you should recognize that the product is advertised as zero sugar and low calorie but may have unnatural ingredients making them this way. You should read the ingredients list and describe the pros and cons for consuming the product. Pros could be it is helpful to getting off soda, but cons could be some of the unnatural ingredients found in the product. Your response should always consider the short term and long term health implications to whatever you are being asked. Your first consumer question is asking about the following product and its ingredients: {product_string}"

        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": initial_prompt}
            ] + [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
