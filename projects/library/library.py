from book import Book
from author import Author


class Library():

    def __init__(self):
        self.authors = []
        self.books = []

    def insert_author(self,first_name,last_name,id):
        self.authors.append(Author(first_name,last_name,id))

    def insert_book(self,title,author):
        self.authors.append(Book(title,author))








