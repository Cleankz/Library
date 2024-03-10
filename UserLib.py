from User import Client
from Literature import Book

class Library():
    def __init__(self, name,adrress, owner, visit_time,):
        """Инициализируем атрибуты"""
        self.name = name
        self.adrress = adrress
        self.owner = owner
        self.visit_time = visit_time
        self.books_num = 0
        self.user_num = 0
