import streamlit as st
import openai
import os


openai_api_key = ("API-KEY")

def get_response(prompt):
    openai.api_key = openai_api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure this is a valid chat model, such as "gpt-4.0-chat"
            messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title('AI Chatbot')
    
    user_input = st.text_input("Search here:", "")

    if user_input:
        bot_response = get_response(user_input)
        st.text_area("ChatGPT:", value=bot_response, height=200, disabled=True)

if __name__ == "__main__":
    main()