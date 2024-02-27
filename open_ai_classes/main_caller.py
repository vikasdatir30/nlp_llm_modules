from open_ai_api_interface import OpenAIInterface
import os
import tomli

def get_config(config_file_path):
    try:
        if os.path.isfile(config_file_path):
            with open(config_file_path, mode='rb') as fptr:
                return tomli.load(fptr)
        else:
            raise Exception('Config File not found')
    except Exception as e:
        print("Error in get_config", e)



def main_caller(_conf):
    try:
        s = OpenAIInterface(_conf)
        print(s.get_token_count("Hello"))
    except Exception as e :
        print("Error in main_caller ", e)





if __name__ == "__main__":
    config_path = os.getcwd() + "/config/config.toml"
    _conf = get_config(config_path)
    main_caller(_conf)