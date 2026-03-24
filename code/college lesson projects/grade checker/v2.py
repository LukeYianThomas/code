boundries = []
gradeList = open("Grades.txt", "a")
def numVal(number,limit):
    while True:
        if 0<= number <= limit:return number
        else:print("Invalid Data")
        number = int(input("Re-Enter data"))
def gradeCalc(mark):
    grade = 10
    for i in range(len(boundries)):
        if mark < boundries[i]:grade-=1
    if grade == boundries[9]:grade = 9
    if grade == 0:grade = "U"
    return grade
for i in range(10):boundries.append(int(input("Enter boundries")))
boundries.reverse
studentCount = numVal(int(input("Enter number of students:")),20)
for i in range(studentCount):
    gradeList.write(input("Enter name: ")+"\n")
    temp = str(gradeCalc(numVal(int(input("Enter mark: ")),boundries[9]))) # MAGIC
    gradeList.write("Grade: "+temp+"\n")
    gradeList.write("========================================="+"\n")
    if temp == "9":gradeList.write("Distinction")
gradeList = open("Grades.txt", "r")
print(gradeList.read())