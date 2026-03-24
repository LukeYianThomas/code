import pandas as pd
df = pd.read_csv("Task3_data.csv")

TotalSales = df["Value"].mean()
SalesPerPerson = df.groupby("Salesperson")["Value"].sum()
SalesPerModel = df.groupby("Car Model")["Value"].sum()
SalesOverTime = df.groupby("Date")["Value"].sum()

def showMenu():
    print("""1 - Show total sales
2 - Show total sales per salesperson
3 - Show total sales per model
4 - Show total sales over time""")
    while True:
        try:
            choice = int(input(""))
            if choice in range(1,4):
                return choice
            else:
                print("Please enter a valid number [1-4]")
        except ValueError:
            print("Please enter a valid number [1-4]")

def showResult(x):
    if x == 1:print(TotalSales)
    if x == 2:print(SalesPerPerson)
    if x == 3:print(SalesPerModel)
    if x == 4:print(SalesOverTime)

showResult(showMenu())