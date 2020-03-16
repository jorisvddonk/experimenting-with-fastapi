from abc import ABC, abstractmethod
 
class Coronauts(ABC):
 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    async def get_cases(self):
        pass

    @abstractmethod
    def get_country_name(self):
        pass
