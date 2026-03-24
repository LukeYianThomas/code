def loyalty_card_check():
    while True:
        cardNumber = input("Enter card  number (8 digits long):")
        if cardNumber.isdigit() and len(cardNumber) == 8:return cardNumber
        else:print("Invalid input please try again")

def get_platform():
    options = ["Online","In-store"]
    for i in range(len(options)):print(f"{i+1}: {options[i]}")
    while True:
        try:
            choice = int(input(f"Enter choice 1-{len(options)}:"))
            if choice in range(len(options)+1):return options[choice-1]
            else:raise ValueError
        except ValueError:print("Invalid selection")

def transactions():
    counter = 1
    options = ["Computing and gaming","Home electrical","Accessories"]
    prices = []
    catagories = []
    while True:
        try:
            print("Enter X to close")
            item = input(f"Enter price of item {counter}: ")
            if item == "X":return prices,catagories
            if int(item) < 0:raise ValueError
            else: prices.append(int(item))
            counter+=1
        except ValueError:print("Invalid price")
        for i in range(len(options)):print(f"{i+1}: {options[i]}")
        print("Catagories:")
        while True:
            try:
                choice = input(f"Enter choice 1-{len(options)}:")
                if int(choice) in range(len(options)+1):break
                else:raise ValueError
            except ValueError:print("Invalid selection")
        catagories.append(options[int(choice)-1])

def main():
    cardNumber = loyalty_card_check()
    platform = get_platform()
    prices,catagories = transactions()
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
    print(f"""Card number: {cardNumber}
Shopping platform: {platform}""")
    for i in purchases:print(i)
    print(f"""Total transaction value: £{sum(prices):.2f}
Total points earned: £{points:.2f}""")

if __name__ == "__main__":main()
        