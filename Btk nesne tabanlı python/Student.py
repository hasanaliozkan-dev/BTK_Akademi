from Person import Person
class Student(Person):

    def __init__(self,name,year,number):
        Person.__init__(self,name,year)
        self.studentNumber = number.split(" ")