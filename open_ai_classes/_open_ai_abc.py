from abc import ABC, abstractmethod


class OpenAI_ABC(ABC):
    @abstractmethod
    def get_token_count(self):
        pass


