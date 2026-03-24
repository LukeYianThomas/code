nameList = []
markList = []
def numVal(number,limit):
    while True:
        if 0<= number <= limit:return number
        else:print("Invalid Data")
def gradeCalc(mark):
    studentGrade = mark // 10
    if studentGrade == 0: studentGrade = "U"
    if studentGrade == 10: studentGrade = 9
    return studentGrade
studentCount = numVal(int(input("Enter number of students:")),20)
for i in range(studentCount):
    nameList.append(input("Enter name: "))
    markList.append(gradeCalc(numVal(int(input("Enter mark: ")),100)))
for i in range(studentCount):print(f"""--------------------------------
{nameList[i]}
Grade {markList[i]}""")