## W modu
"""file = open("newfile.txt","w")
file.close()
print(file)"""
"""
file = open("/Users/hasanaliozkan/Desktop/PythonFile.txt","w")
file.close()
print(file)
"""
"""
file = open("newfile.txt","w")
file.write("hasanaliozkan")
file.close()"""
## A modu
"""file = open("newfile.txt","a")
file.write("\nbüşraerturan")
file.close()
"""
## X modu
"""
file = open("newfile.txt","x")
print(file)"""
## r modu
"""try:
    file = open("newfile2.txt","r")
    print(file)
except FileNotFoundError:
    print("File Reading Fault")

"""
file = open("newfile.txt","r",encoding="utf-8") ## default is 'r'
## with for loop
"""
for line in file:
    print(line,end="")
file.close()"""
## with read()
"""content = file.read()
print(content)
content = file.read(5)
content = file.read(3)
print(content)"""
## with readline()
"""print(file.readline(),end="")
print(file.readline(),end="")"""
## with readlines()
"""contentlist = file.readlines()
print(contentlist)"""


"""with open("newfile.txt","r") as file:
    content = file.read()
    print(content)
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2)"""



