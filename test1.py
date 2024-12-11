class Student:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def info(self):
        print(f"Student ismi: {self.name}, Telefon raqami: {self.phone}")
    def get_name(self):
        print(self.name)


student = Student("Abdyazim","+998909119091")
student.get_name()