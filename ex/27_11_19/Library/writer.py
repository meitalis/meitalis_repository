class Writer():

    def __init__(self, first_name,last_name,id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self,first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self,last_name):
        self.__last_name = last_name

    @property
    def id(self):
        return self.__id

    @last_name.setter
    def id(self, id):
        self.__id = id

