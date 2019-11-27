import uuid


class Book():

    def __init__(self, title,author_id):
        self.title = title
        self.author_id = author_id
        self.uuid1 = uuid.uuid1()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        self.__title = title

    @property
    def author_id(self):
        return self.__author_id

    @author_id.setter
    def author_id(self,author_id):
        self.__author_id = author_id



