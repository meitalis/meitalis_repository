import uuid


class Book():

    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.uuid1 = uuid.uuid1()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self,author):
        self.__author = author

    def print(self):
        print(f"title {self.title} author {self.author} uuid1 {self.uuid1}")




