def get_platform():
    while True:
        try:
            option = int(input("""Please select a purchase platform:
1. Online
2. In-Store\n"""))
            if option == 1:return "Online"
            elif option == 2:return "In-Store"
            else:print("Invalid option")
        except ValueError:print("Invalid option, must be a number.")
    
def loyalty_card_check():
    while True:
        card_number = input("Please enter the loyalty card number (8 digits): ")
        if card_number.isdigit() and len(card_number) == 8:return card_number
        else:print("Invalid card number, must be exactly 8 digits.\n")

def get_items(prices,catagories):
    item_count = 1
    while True:
        try:
            temp_price = input(f"Enter price for item {item_count} (or X to finish).£")
            if temp_price.upper() == "X":return
            price = float(temp_price)
            if price <= 0:raise ValueError
            item_count += 1
        except ValueError:print("Invalid input, enter either a positive number or X to finish.")
        while True:
            print("""Select category:
    1. Home Electrical
    2. Computing and Gaming
    3. Accessories and consumables""")
            choice = input("Catagory:")
            if choice == "1":
                catagory = "Home Electrical"
            elif choice == "2":
                catagory = "Computing and Gaming"
            elif choice == "3":
                catagory = "Accessories and consumables"
            else:
                print("Invalid catagory try again.")
            prices.append(price)
            catagories.append(catagory)
            break
        
def calculate_points(prices, catagories):
    points_earned = []
    
    for i in range(len(prices)):
        value = int(prices[i])
        category = catagories[i]
        if category == "Computing and Gaming":
            if value > 500:pts = 2000 +((value - 500) * 2)
            else:pts = value * 4
        elif category == "Home Electrical":pts = value * 4
        else:pts = value * 3
        points_earned.append(pts)
    return points_earned

def main():
    prices = []
    catagories = []
    
    card_number = loyalty_card_check()
    platform = get_platform()
    get_items(prices,catagories)
    if not prices:
        print("No items entered. Transaction cancelled.")
        return
    points_earned = calculate_points(prices,catagories)
    total_value = sum(prices)
    points_subtotal = sum(points_earned)
    if platform == "In-Store":bonus_pts = int(total_value) * 2
    else:bonus_pts = 0
    final_pts = points_subtotal + bonus_pts
    print(f"""------------------------------------------------------------
Transaction summary for customer {card_number}
------------------------------------------------------------
Total transaction value: £{total_value:.2f}
Points earned per item:""")
    for i in range(len(points_earned)):
        print(f"Item {i+1}: {points_earned[i]} pts")
    print(f"""------------------------------------------------------------
Points subtotal: {points_subtotal}
Bonus points earned: {bonus_pts}
------------------------------------------------------------
Final total points: {final_pts}
------------------------------------------------------------""")


if __name__ == "__main__":main()