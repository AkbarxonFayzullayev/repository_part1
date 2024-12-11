class User:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    def get_name(self):
        print(f"User ismi: {self.name}")
user1 = User("Asror","Xasanov")
user1.get_name()