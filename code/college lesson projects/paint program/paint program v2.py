METRE_PER_LITRE = 5
DOOR_AREA = 2.5
LABOUR_COST_PER_METRE = 2
COST_5LTR_TIN = 50
COST_3LTR_TIN = 35
COST_2LTR_TIN = 25
COST_1LTR_TIN = 15
while True:
    numWalls = int(input(' Enter number of walls: '))
    if  0< numWalls <= 20:
            break
    else:
        print(' Invalid data, please enter a new number (between 1-20)' )
print(' Valid ')
total_Paint_Area = 0
for i in range(1,numWalls+1):
    lenWall = float(input(" Please enter the length of the walls: "))
    widWall = float(input(" Please enter the width of the walls: "))
    wallAr = lenWall*widWall

    doorTrue = input("Is there a door")
    if doorTrue.lower() == "yes":
        DOOR_AREA = 2.5
    else:
        DOOR_AREA = 0
        
    lenWin = float(input(" Please enter the length of the windows: "))
    widWin = float(input(" Please enter the width of the windows: "))
    winAr = lenWin*widWin

    paint_Area = wallAr - DOOR_AREA - winAr
    total_Paint_Area += paint_Area
print('Total paint area : ',total_Paint_Area)

litresPaint = int(round(total_Paint_Area/METRE_PER_LITRE))    

x = litresPaint//5
remainder = litresPaint % 5

x2 = remainder//3
remainder = litresPaint % 3

x3 = remainder//2
remainder = litresPaint % 2
x4 = remainder//1
print(f"""==========================
there are:
{x} x 5L tins
{x2} x 3L tins
{x3} x  2L tins
{x4} x 1L tins
labour costs:
£{LABOUR_COST_PER_METRE*total_Paint_Area}
 paint costs:
 £{x*COST_5LTR_TIN+x2*COST_3LTR_TIN+x3*COST_2LTR_TIN+x4*COST_1LTR_TIN}
 ==========================
""")
