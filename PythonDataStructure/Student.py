class Person:
    age= 0
    name = ""
    def __init__(self,name,age):
        print("Person Created")
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        print("Student Created")




