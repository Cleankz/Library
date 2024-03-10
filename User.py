
class Client():

    def __init__(self, firstname,lastname, age, birthday,regdate,email, phone, residential_address):
        """Инициализируем атрибуты """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.birthday = birthday
        self.regdate = regdate
        self.email = email
        self.phone = phone
        self.residential_address = residential_address
        self.in_library = False

    def take_book(self):
        """Посетитель берет книгу"""
        ...
    def return_book(self):
        """Посетитель возвращает книгу"""
        ...

