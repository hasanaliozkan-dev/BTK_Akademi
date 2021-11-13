import datetime
class Person():
    #atributes
    adress = "-----------"
    #constructor
    def __init__(self,name,year):
        ##objectatributes
        self.name = name.title()
        self.year = year
    def __len__(self):
        return len(self.name)
    def age(self):
        return datetime.datetime.now().year - self.year



