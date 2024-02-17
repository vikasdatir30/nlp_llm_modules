"""
Script Name: chat_bot_app.py
Author: Vikas Datir
Date: 07/02/2024
Last Modified: 17/02/2024
Purpose: A chatbot to demonstrate use of pandasai
"""

import streamlit as st
import os
from pandasai.helpers.openai_info import get_openai_callback
from pandasai import SmartDataframe
import pandas as pd
from pandasai.llm.openai import OpenAI

file_store_path = "file_storage"
file_select = ""

openai_api_key = os.environ['OPENAI_API_KEY']


# file uploading  and saving
def get_files_in_folder(folder_path):
    file_paths = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                file_paths.append(file_path)

    return file_paths


def create_folder(folder_name):
    try:
        folder_path = os.path.join(file_store_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created at '{os.path.abspath(folder_path)}'")
        else:
            print(f"Folder '{folder_name}' already exists at '{os.path.abspath(folder_path)}'")

        return str(os.path.abspath(folder_path))
    except Exception as e:
        print("Error in create_folder : ", e)


def upload_file_to_storage(uploaded_file):
    try:
        file_name = uploaded_file.name.split('.')[0]
        file_path = create_folder(file_name) + '\\' + uploaded_file.name
        with open(file_path, mode="wb") as fptr:
            fptr.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        print("Error in ", e)


# PandasAI + OpenAI
def generate_response(question):
    try:
        file_list = get_files_in_folder(file_store_path + "/" + os.path.basename(file_select))
        raw_df = pd.read_csv(file_list[0], sep=',')

        print(raw_df)
        llm = OpenAI(openai_api_key)
        df = SmartDataframe(raw_df, config={"llm": llm, "conversational": False, "model": "GPT-3.5-turbo-0613"})

        with get_openai_callback() as cb:
            response = df.chat(question)
            print(response)
        return response
    except Exception as e:
        print("Error in generate_response", e)


def chat_interface():
    global file_select
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload Data file", type=['.csv'], accept_multiple_files=False)
        upload_button = st.button('Upload')
        if upload_button:
            if uploaded_file is not None:
                file_path = upload_file_to_storage(uploaded_file)
            else:
                st.error('Upload valid file')

        file_select = st.selectbox("Select file", options=os.listdir(file_store_path))

    prompt = st.text_area("Enter your prompt:")
    # Generate output
    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(generate_response(prompt))
        else:
            st.warning("Please enter a prompt.")


if __name__ == "__main__":
    chat_interface()
