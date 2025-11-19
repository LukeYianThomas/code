def totalPaintAreaCalc(lenWall,widWall,doorExist,lenWin,widWin):
    wallArea = widWall*lenWall
    winArea = widWin*lenWin
    if doorExist.lower() == "yes":
        widDoor,lenDoor = input("Enter door dimensions").split(",")
        doorArea = float(widDoor)*float(lenDoor)
    else:doorArea = 0
    paintArea = wallArea-winArea-doorArea
    return paintArea

print(totalPaintAreaCalc(20,20,"yes",10,10))