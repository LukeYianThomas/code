#Standard sizes and cost of pizzas
SMALL_COST = 3.25
MEDIUM_COST = 5.50
LARGE_COST = 7.15

#Cost of any extra toppings
EXTRA_TOPPING_1 =  0.75
EXTRA_TOPPING_2 = 1.35
EXTRA_TOPPING_3 = 2.00
EXTRA_TOPPING_4 = 2.50

#Discount for orders over £20
DISCOUNT = 0.1

#Standard delivery charge
DELIVERY_CHARGE = 2.50

MIN_NUMBER_PIZZAS = 1
MAX_NUMBER_PIZZAS = 6

#Collects information
name = str(input("Enter name: "))
address = str(input("Enter address: "))
phone = int(input("Enter phone number: "))

def validate_quantity_range(qty):
    while not qty in range(MIN_NUMBER_PIZZAS,MAX_NUMBER_PIZZAS):qty = int(input("Invalid Data , please re-enter:"))
    return qty
    
quantity = int(input("Enter number of pizzas small/medium/large: "))
quantity = validate_quantity_range(quantity)

totalCost = 0
for i in range(1, quantity+1):
    size = str(input("Enter size: "))
    numToppings = int("Enter number of toppings: ")
    delivery = str(input("Order for delivery?: "))
    if size == "small":
        baseCost = SMALL_COST
    elif size == "medium":
        baseCost = MEDIUM_COST
    elif size == "large":
        baseCost = LARGE_COST 
    if numToppings == 1:
        toppingsCost = EXTRA_TOPPING_1
    elif numToppings == 2:
        toppingsCost = EXTRA_TOPPING_2
    elif numToppings == 3:
        toppingsCost = EXTRA_TOPPING_3
    else:
        toppingsCost = EXTRA_TOPPING_4

    pizzaCost = baseCost+toppingsCost

    totalCost = totalCost + pizzaCost

if totalCost>= 20:
    totalCost = totalCost - totalCost*DISCOUNT

deliveryCost = 0
if delivery == "Yes":
    deliveryCost = DELIVERY_CHARGE

#Outputs the bill
print(f"""----BILL----
Customer name: {name}
Address: {address}
Phone number: {phone}
Subtotal: {totalCost}
Delivery charge: {deliveryCost}
Total: {totalCost+deliveryCost}""")