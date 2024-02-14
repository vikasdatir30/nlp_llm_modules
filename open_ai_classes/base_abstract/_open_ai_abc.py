"""
Script Name: _open_ai_abc.py
Author: Vikas Datir
Date: 14/02/2024
Last Modified: 14/02/2024
Purpose: An abstract class created to define interface for OPENAI APIs.
"""




from abc import ABC, abstractmethod


class OpenAI_ABC(ABC):
    @abstractmethod
    def get_token_count(self, input_text):
        pass


