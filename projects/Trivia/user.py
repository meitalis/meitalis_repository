class User():

    def __init__(self, full_name,id):
        self.__full_name = full_name
        self.__id = id

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self,full_name):
        self.__full_name = full_name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

