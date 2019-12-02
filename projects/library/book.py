import uuid


class Book():

    def __init__(self, title,author):
        self._title = title
        self._author = author
        self.uuid1 = uuid.uuid1()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,author):
        self._author = author

    def print(self):
        print(f"title {self.title} author {self.author} uuid1 {self.uuid1}")




