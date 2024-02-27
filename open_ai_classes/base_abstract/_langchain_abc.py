"""
Script Name: _open_ai_abc.py
Author: Vikas Datir
Date: 27/02/2024
Last Modified: 27/02/2024
Purpose: An abstract class created to define interface for OPENAI APIs.
"""



from abc import ABC,abstractmethod


class Langchain_ABC(ABC):
    @abstractmethod
    def test(self):
        pass