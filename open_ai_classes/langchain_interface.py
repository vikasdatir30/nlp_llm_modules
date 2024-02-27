# from langchain import PromptTemplate, LLMChain
# from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.callbacks import get_openai_callback
# from langchain.chains.question_answering import load_qa_chain
# from langchain.document_loaders import PyPDFLoader
# from langchain.docstore.document import Document
# from langchain.vectorstores.faiss import FAISS
from base_abstract._langchain_abc import Langchain_ABC

import os
import logging
from datetime import datetime as dt

run_date = str(dt.now().strftime("%Y_%m_%d_%H%M%S"))

logging.basicConfig(level=logging.INFO)


class LangchainInterface(Langchain_ABC):
    def __init__(self):
        try:
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


        except Exception as e:
            self.logger.error(str(e) + " - Failed to initialize LangChainInterface.")
