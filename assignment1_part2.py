#!/usr/bin/python
# -*- coding: utf-8 -*-

class Book:
    """
    A class with parameters describing a book's traits

    attr1: str
        Author of the book
    attr2: str
        Title of the book

    """
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        """
        Displays the title and author
        """
        print(f'{self.title}, written by {self.author}')


firstBook = Book('John Steinbeck', 'Of Mice and Men')
secondBook = Book('Harper Lee', 'To Kill a Mockingbird')

firstBook.display()
secondBook.display()


