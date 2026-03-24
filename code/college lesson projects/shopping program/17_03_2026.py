#Q1
def loyalty_card_check():
    while True:
        cardNumber = input("Enter card  number (8 digits long):")
        if cardNumber.isdigit() and len(cardNumber) == 8:return cardNumber
        else:print("Invalid input please try again")
#Q2
def get_platform():
    options = ["Online","In-store"]
    for i in range(len(options)):print(f"{i+1}: {options[i]}")
    while True:
        try:
            choice = int(input(f"Enter choice 1-{len(options)}:"))
            if choice in range(len(options)+1):return options[choice-1]
            else:raise ValueError
        except ValueError:print("Invalid selection")
        
#Q3
def unnamed():
    counter = 1
    prices = []
    while True:
        try:
            item = input(f"Enter price of item {counter}: ")
            if item == "X":return prices
            if int(item) < 0:raise ValueError
            else: prices.append(int(item))
            counter+=1
        except ValueError:print("Invalid price")

#Q4
#Already done above ^

#Q5
def catagoryDisplay():
    options = ["Catagory 1","Catagory 2","Catagory 3"]
    catagories = []
    for i in range(len(options)):print(f"{i+1}: {options[i]}")
    while True:
        try:
            choice = input(f"Enter choice 1-{len(options)}:")
            if choice == "X":return catagories
            if int(choice) in range(len(options)+1):catagories.append(options[int(choice)-1])
            else:raise ValueError
        except ValueError:print("Invalid selection")

#Q6
#catagories = catagoryDisplay()
#prices = unnamed()

#Q7 Q8 Q9
cardNumber = loyalty_card_check()
catagories = catagoryDisplay()
prices = unnamed()
platform = get_platform()
purchases = []
points = 0
for i in range(len(prices)):
    prices[i]
    catagories[i]
    purchases.append(f"{catagories[i]} - £{prices[i]:.2f}")
    if catagories[i] == "Computing and gaming":
        if prices[i]<500:points+=prices[i]*4
        elif platform == "In-store":points+=prices[i]*8
    if catagories[i] == "Home electrical":points+=prices[i]*4
    if catagories[i] == "Accessories":points+=prices[i]*3
    
#Q10
def recipt():
    print(f"""Card number: {cardNumber}
Shopping platform: {platform}""")
    for i in purchases:print(i)
    print(f"""Total transaction value: £{sum(prices):.2f}
Total points earned: £{points:.2f}""")
