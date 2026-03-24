from datetime import datetime

products = [
    ["Lenevo AS12",750.00,5],
    ["MSI RF4",1050.00,7]
]

sales = []

def stockCheck():
    print("\nCurrent Stock:")
    print("[Product, Price, Stock]")
    for item in products:
        print(f"{item[0]} - £{item[1]:.2f} - {item[2]} in stock")
    input()

def addStock():
    stock_type = input("Enter product name: ").title()
    while True:
        try:
            cost = round(float(input("Enter product cost (2 decimal places): ")), 2)
            break
        except ValueError:
            print("Enter a valid number")
    while True:
        try:
            stock = int(input("Enter amount of stock:"))
            if stock < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid stock amount")
    products.append([stock_type, cost, stock])
    print("Stock added successfully.\n")
    input()

def recordSale():
    sale_data = []
    
    
    date_time = datetime.now(strftime("%d/%m/%Y"))
    print(date_time)
    while True:
        product = addition()
        items.append(product)
        
        total_quantity += product[1]
        sub_total += calculate_price(product)

def addition():
    while True:
        product_name = input("Enter product name: ")
        found = False
        
        for item in products:
            if product_name.lower() == item[0.lower()]:
                found = True
                while True:
                    try:
                        quantity = int(input(f"Enter amount to buy: "))
                        if quantity < 1:raise ValueError
                        
                    except ValueError:
                        print("Invalid quantity")

def calculate_price():
    pass

while True:
    try:
        option = int(input("""Enter 1 for Stock Check
Enter 2 to Add stock
Enter 3 to Record Sale
Enter 4 to Exit\n"""))

        if option == 1:
            stockCheck()
        elif option == 2:
            addStock()
        elif option == 3:
            recordSale()
        elif option == 4:
            print("Exiting program")
            break
        else:
            print("Please enter a number 1-4")
    except ValueError:
        print("Enter a valid number")