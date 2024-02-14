"""
Script Name: _open_ai_abc.py
Author: Vikas Datir
Date: 14/02/2024
Last Modified: 14/02/2024
Purpose: A OpenAI_API_Interface class defined using abstract class to implement required methods
"""


from _open_ai_abc import OpenAI_ABC
from openai import OpenAI
import tiktoken as tkn
import os
import tomli

class OpenAI_API_Interface(OpenAI_ABC):
    def __init__(self, config:dict):
        self.open_ai_config = config['open_ai']
        try:
            if "OPENAI_API_KEY" in os.environ.keys():
                self.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

            elif "OPENAI_API_KEY" in self.open_ai_config.keys():
                self.OPENAI_API_KEY = self.open_ai_config['OPENAI_API_KEY']

            else:
                raise Exception('OPENAI_API_KEY is not set')

        except Exception as e:
            print("Error in  ", e)

    def get_token_count(self):
        pass



def get_config(config_file_path):
    try:
        if os.path.isfile(config_file_path):
            with open(config_file_path, mode='rb') as fptr:
                return tomli.load(fptr)
        else:
            raise Exception('Config File not found')
    except Exception as e:
        print("Error in get_config", e)



if __name__ =="__main__":
    config_path = os.getcwd() + "/config/config.toml"
    _conf = get_config(config_path)
    s = OpenAI_API_Interface(_conf)