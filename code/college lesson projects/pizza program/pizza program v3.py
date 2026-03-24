dataList = ["small","medium","large",0.75,1.35,2,2.5]
name = input("Enter name: ")
address = input("Enter address: ")
phone_number = input("Enter phone number: ")
numPizza = int(input("Enter number of pizzas: "))
while not numPizza in range(1,6):numPizza = int(input("Invalid data, please try again: "))
delivery = input("Delivery: ").lower()
while not ((delivery == "no") or (delivery == "yes")): delivery = input("Invalid data, please try again: ").lower()
with open("recipt.txt", "r+") as recipt:
    recipt.seek(0)
    recipt.truncate()
def pizzaCalc():
    size = input("Enter the size of pizza: ").lower()
    while not size in dataList:size = input("Invalid data, please try again: ").lower()
    if size == "small":pizza = 3.25
    elif size == "medium":pizza = 5.50
    else:pizza = 7.15
    toppingCount = int(input("Enter number of toppings: "))
    if toppingCount == 0: toppingPrice = 0
    elif toppingCount<=4:toppingPrice = 1*dataList[toppingCount+2]
    else:toppingPrice = 2.50
    return size,pizza,toppingPrice,toppingCount
recipt = open("recipt.txt", "a")
totalPrice = 0
recipt.write(f"""===================
Pizza Shop
===================
Name: {name}
Address: {address}
Phone: {phone_number}
Delivery: {delivery}     
""")
for i in range(numPizza):
    tempSize,tempPizza,tempToppings,tempToppingCount = pizzaCalc()
    temp = (f"{tempSize} pizza: £{tempPizza}"+"\n")
    recipt.write(temp)
    temp = (f"{tempToppingCount} toppings: £{tempToppings}"+"\n")
    recipt.write(temp)
    totalPrice+=tempPizza+tempToppings
if totalPrice >= 20:
    recipt.write(f"DISCOUNT [10%]"+"\n")
    totalPrice*0.9
if delivery == "yes":
    recipt.write(f"delivery fee: £2.50"+"\n")
    totalPrice += 2.5
recipt.write(f"TOTAL PRICE: £{totalPrice}")
recipt.close()
with open("recipt.txt", "r") as recipt:
    content = recipt.read()
    print(content)