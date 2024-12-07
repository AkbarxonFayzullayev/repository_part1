from test import Person

class Student(Person):
    def __init__(self,name,phone,adres):
        super().__init__(name,phone)
        self.adres = adres