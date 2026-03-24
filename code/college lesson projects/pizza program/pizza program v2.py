dataList = ["small","medium","large",0,0,0.9,0.85,0.85,0.8]
size = input("Enter the size of pizza").lower()
while not size in dataList:size = input("Invalid data, please try again: ").lower()
if size == "small":pizza = 5.99
elif size == "medium":pizza = 8.99
else:pizza = 11.99
toppingCount = int(input("Enter number of toppings"))
while not 0<=toppingCount<=5:toppingCount = int(input("Invalid data, please try again: "))
toppingPrice = toppingCount*1.20*dataList[toppingCount+3]
print(f"Total cost : £{toppingPrice+pizza}")