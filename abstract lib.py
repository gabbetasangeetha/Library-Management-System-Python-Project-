from abc import ABC, abstractmethod

class User(ABC):
    def _init_(self, user_id, name):
        self.user_id = user_id
        self.name = name
    
    @abstractmethod
    def get_details(self):
        pass