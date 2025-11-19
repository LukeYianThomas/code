# creating a list to store the upper boundries of grades
boundries = []

# this function takes a number and a limit and returns the number if it is within 0 and the limit otherwise asks the user to re enter a number
def numVal(number,limit):
    while True:
        if 0<= number <= limit:return number
        else:print("Invalid Data")
        number = int(input("Re-Enter data"))

# Appends 10 boundries to the boundries list
for i in range(10):boundries.append(int(input("Enter boundries")))

#list is reversed to simplify the process of checking grades
boundries.reverse

# calls the numVal function with number as the user's input and the limit as the item at the 9th index in the boundries list and stores it as mark
mark = numVal(int(input("Enter mark: ")),boundries[9])

# grade is assigned 10 and loops 10 times checking each time if the mark is smaller than a boundry , if it is the grade is decreased by 1
grade = 10
for i in range(len(boundries)):
    if mark < boundries[i]:
        grade-=1
if grade == boundries[9]:
    grade = 9
if grade == 0:
    grade = "U"

# outputs grade
print("Grade: ",grade)
