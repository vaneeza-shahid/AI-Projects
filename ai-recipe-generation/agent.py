import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_response(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Recipe-GPT whose goal is to aid users with recipe-related questions. 
        Make sure to introduce yourself in your initial message."""})
    response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages
            )
    return response.choices[0].message.content

def generate_stream(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Recipe-GPT whose goal is to aid users with recipe-related questions. If a user 
        asks for information about a recipe, give a brief description, then list the ingredients of recipe, the complete procedure of recipe,
        its cooking time and the effectiveness of the recipe using quantitative values. Also, list the relevant recipes along with a brief description of each. Do not respond to off-topic inquiries"""})
    stream = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=0.1,
                stream=True,
            )
    return stream
