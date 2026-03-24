#CONSTANTS to make it easier to change and for readability
METRE_PER_LITRE = 5
DOOR_AREA = 2.5
LABOUR_COST_PER_METRE = 2
COST_5LTR_TIN = 50
COST_3LTR_TIN = 35
COST_2LTR_TIN = 25
COST_1LTR_TIN = 15

#The following function accepts the amount of paint required from previous calculations and copies the variable into the function variable and returns the total cost of paint
#It does this by dividing by 5 then modulus by 5 then dividing by 3 and modulus by 3 etc to work out the number of each tins required
#It will then use the appropriate formula to calculate the total cost of paint
def paintPrice(litresPaint):
    global x,x2,x3,x4
    x = litresPaint//5
    remainder = litresPaint % 5
    x2 = remainder//3
    remainder = litresPaint % 3
    x3 = remainder//2
    remainder = litresPaint % 2
    x4 = remainder//1
    total_Paint_Cost= x*COST_5LTR_TIN+x2*COST_3LTR_TIN+x3*COST_2LTR_TIN+x4*COST_1LTR_TIN
    return total_Paint_Cost

#The following function accepts these values from the main program and copies the variable into the function variables and calculates the paintArea
def totalPaintAreaCalc(lenWall,widWall,doorExist,lenWin,widWin):
    wallArea = widWall*lenWall
    winArea = widWin*lenWin
    if doorExist.lower() == "yes":
        widDoor,lenDoor = input("Enter door dimensions").split(",")
        doorArea = float(widDoor)*float(lenDoor)
    else:doorArea = 0
    paintArea = wallArea-winArea-doorArea
    return paintArea

#The following function accepts the value of number of walls in the main program and copies the variable to the function variable and checks if it is within the range and breaks and if not it prints invalid data
def numDataVal(numWalls):
    while True:
        if  0< numWalls <= 20:
            break
        else:
            print(' Invalid data, please enter a new number (between 1-20)' )
    return




numWalls = int(input(' Enter number of walls: '))
print(totalPaintAreaCalc(20,20,"yes",10,10))
numDataVal(numWalls)
print(' Valid ')

# This algorithm repeatedly asks the user for measurements of the dimensions and pass them into the total paint function and adds the return value to the total_paint_area variable
total_Paint_Area = 0
for i in range(1,numWalls+1):
    lenWall = float(input(" Please enter the length of the walls: "))
    widWall = float(input(" Please enter the width of the walls: "))
    doorExist = input("Is there a door")  
    lenWin = float(input(" Please enter the length of the windows: "))
    widWin = float(input(" Please enter the width of the windows: "))
    total_Paint_Area += totalPaintAreaCalc(lenWall,widWall,doorExist,lenWin,widWin)

print('Total paint area : ',total_Paint_Area)
#The following formulas calculates the total cost
litresPaint = int(round(total_Paint_Area/METRE_PER_LITRE))    
labourCost = total_Paint_Area*LABOUR_COST_PER_METRE
paintCost = paintPrice(litresPaint)
totalcost = labourCost+paintCost
print(f'The paint costs £',paintCost)
print(f'The labour costs £',labourCost)
print(f'The total cost is £',totalcost)