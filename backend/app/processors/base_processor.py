from abc import (
    ABC,
    abstractmethod
)

class BaseProcessor(ABC):

    @abstractmethod
    def extract_text(self,file_path:str) -> list[dict]:

        pass