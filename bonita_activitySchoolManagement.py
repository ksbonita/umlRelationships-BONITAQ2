# excer1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")

person1 = Person("Mona Lina G. Albarracin", 20)
person1.display_info()

# excer2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.get_age()} (note this age is privately accessed)")

person2 = Person("Mona Lina G. Albarracin II", 20)
person2.display_info()

# my reflection: it is better to access __age through get_age() so age data stays protected and cannot be accidentally changed from outside the class.

#excer 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()} (note this age is privately accessed)")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying")


student1 = Student("Mona Lina G. Albarracin Jr", 20)
student1.display_info()
student1.study()
