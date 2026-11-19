class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")

#gwaposikyle

person1 = Person("Mona Lina G. Albarracin", 20)

person1.display_info()