from enum import Enum

class AnimalsParser():

    class __Animal(Enum):
        MAMMAL = 1
        REPTILE = 2
        BIRD = 3

    def __init__(self,fp):
        self.__fp = fp
        self.parse()
        self.__creators = {}

    def parse(self):
        self.register_animals()
        pass

    def register_animal(self):
        if (e_animal == AnimalsParser.__Animal)
        self._creators[e_animal] = creator

    def get_animal(self, e_animal):
        creator = self._creators.get(e_animal)
        if not creator:
            raise ValueError(e_animal)
        return creator()

