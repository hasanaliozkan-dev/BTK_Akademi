def writeGrade():
    name = input("Name:")
    surname = input("Surname:")
    grade1 = input("Grade1:")
    grade2 = input("Grade2:")
    grade3 = input("Grade3:")
    with open("Grades.txt","a") as file:
        file.write(name+" "+surname+":"+grade1+","+grade2+","+grade3+"\n")

def average(line):
    line = line[:-1]
    list = line.split(':')
    name = list[0]
    grades = list[1].split(',')
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])
    avg = (grade1 + grade2 + grade3)//len(grades)
    alpha = ''
    if avg>=90 and avg<=100:
        alpha = 'AA'
    elif avg>=85 and avg<=89:
        alpha = 'BA'
    elif avg>=65:
        alpha = 'CC'
    else:
        alpha = 'FF'
    return name +' : '+ alpha + '\n'
def readGrade():
    with open("Grades.txt","r") as file:
        for line in file:
            print(average(line),end='')
def saveGrades():
    with open("Grades.txt","r") as file:
        lineList = list()
        for i in file:
            lineList.append(average(i))

    with open("Alphas.txt","w") as file2:
        for i in lineList:
            file2.write(i)


while True:
    procces = input("1- Notları oku.\n2- Not gir.\n3- Notları kaydet.\n4- Çıkış\n")

    if procces == '1':
        readGrade()
    elif procces == '2':
        writeGrade()
    elif procces == '3':
        saveGrades()
    else:
        break
