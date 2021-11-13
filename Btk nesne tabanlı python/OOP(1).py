'''from Person import Person
from Student import Student
p1 = Person("ali",1999)
p1.adress = "Meram/KONYA"
s1 = Student("öğrenci ali",1999,"180709020")
s1.adress = "Menteşe/MUĞLA"

print((f"Name: {p1.name} \nBirthYear: {p1.year} \nAdress: {p1.adress} \nAge: {p1.age()}"))
print(p1.__len__())
print((f"Name: {s1.name} \nBirthYear: {s1.year} \nAdress: {s1.adress} \nAge: {s1.age()}\nStudent Number: {s1.studentNumber}"))'''
###Modül import etme yöntemleri ###
#Yöntem 1#
# import modulismi as kullanılacakisim#
#Yöntem 2#
# from modülismi import *(herhangi bir isim kullanmadan methodlar çağrılabilir)
# (tüm methodlar import edilmiş oluyor tek tek methodlarıda import edebilirsin)
'''Encapsulation'''
def outerFunc(num1):
    def innerFunc(num1):
        return num1 + 1
    num2 = innerFunc(num1)
    print(num1,num2)

outerFunc(10)