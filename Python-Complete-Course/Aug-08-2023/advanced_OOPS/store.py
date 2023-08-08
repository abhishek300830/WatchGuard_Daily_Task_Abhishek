from database import Database
from saveable import Saveable


class Store(Saveable):

    def to_dict(self):
        pass

    # def save(self):
    #     Database.insert(self.to_dict())