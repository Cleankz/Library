class Book():

    def __init__(self, name,book_series,publishing_house, receipt_date, rent_price):
        """Инициализируем атрибуты"""
        self.name = name
        self.book_series = book_series
        self.publishing_house = publishing_house
        self.receipt_date = receipt_date
        self.rent_price = rent_price
        self.rent_date = 0
        self.rented = False

    def rent_book(self):
        """Посетитель берет книгу"""
        ...
    def return_book(self):
        """Посетитель возвращает книгу"""
        ...
    def write_off_book(self):
        """Библиотекарь списывает книгу"""
        ...
    def accept_book(self):
        """Библиотекарь принимает новую книгу"""
        ...