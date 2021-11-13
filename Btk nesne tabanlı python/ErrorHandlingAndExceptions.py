'''mylist = ['1','2','5a','10b','abc','10','50']
for item in mylist:

    try:
        print(int(item))
    except ValueError:
        continue


while True:
    x = input("sayı:")
    if x == "q":
        break
    try:
        x = int(x)
    except ValueError as a:
        print(a)
'''
def checkPasword(pasword):
    turkishCharacter = ['ö','Ö','ü','Ü','İ','ı','ç','Ç','ğ','Ğ','ş','Ş']
    for chr in pasword:
        if chr in turkishCharacter:
            raise TypeError("Parola connot contain Turkish character!!!")
        else:
            pass
    print("parola is valid")
pasword = input("Password: ")
try:
    checkPasword(pasword)
except TypeError as a:
    print(a)



