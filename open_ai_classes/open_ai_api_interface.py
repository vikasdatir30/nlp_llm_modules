"""
Script Name: _open_ai_abc.py
Author: Vikas Datir
Date: 14/02/2024
Last Modified: 27/02/2024
Purpose: A OpenAiInterface class defined using abstract class to implement required methods
"""
from abc import ABC
from base_abstract._open_ai_abc import OpenAI_ABC
from openai import OpenAI, OpenAIError
import tiktoken as tkn
import os
import logging
from datetime import datetime as dt

run_date = str(dt.now().strftime("%Y_%m_%d_%H%M%S"))

logging.basicConfig(level=logging.INFO)


class OpenAIInterface(OpenAI_ABC, ABC):
    def __init__(self, config: dict):
        self.logger = logging.getLogger("OpenAiInterface")
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler and set the level to debug
        log_file = "OpenAiInterface_log_" + run_date + ".log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create a formatter and set the formatter for the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(file_handler)

        self.open_ai_config = config['open_ai']
        try:

            # searching key in env variables or in config
            if "OPENAI_API_KEY" in os.environ.keys():
                self.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
                self.logger.info("OPENAI_API_KEY found in environment variable")
                self.open_ai_client = OpenAI(api_key=self.OPENAI_API_KEY)

            elif "OPENAI_API_KEY" in self.open_ai_config.keys():
                self.OPENAI_API_KEY = self.open_ai_config['OPENAI_API_KEY']
                self.logger.info("OPENAI_API_KEY found in config variable")
                self.open_ai_client = OpenAI(api_key=self.OPENAI_API_KEY)

            else:
                raise Exception("OPENAI_API_KEY not found")

        except OpenAIError as e:
            self.logger.error(str(e) + " - Please set OPENAI_API_KEY key in env variable or in config file.")

    def get_openai_client(self):
        return self.open_ai_client

    def get_token_count(self, input_text) -> int:
        try:
            """Returns the number of tokens for a input string."""
            encoding = tkn.encoding_for_model(self.open_ai_config['llm_model'])
            num_tokens = len(encoding.encode(input_text))
            return num_tokens
        except Exception as e:
            self.logger.error("Error in get_token_count method - "+str(e))

    def get_chat_prompt_template(self, system_content, user_content):
        try:
            prompt_template =[
                {
                    "role": "system",
                    "content": system_content
                },
                {
                    "role": "user",
                    "content": user_content
                }
            ]

            return prompt_template
        except Exception as e:
            self.logger.error("Error in get_chat_prompt_template method - " + str(e))

    def get_text_embeddings(self, input_text):
        try:
            return self.open_ai_client.embeddings.create(model=self.open_ai_config['embedding_model'], input=input_text )
        except Exception as e :
            self.logger.error("Error in get_text_embeddings method - " + str(e))

if __name__ == "__main__":
    pass

