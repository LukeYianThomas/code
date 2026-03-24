houses = [
    ['LONDON','Terraced',3,735000],
    ['CARDIFF','Semi-Detatched',2,100000],
    ['LEEDS','Terraced',3,245000],
    ['LONDON','Semi-Detatched',1,240000]
] # added commas
sales = []
ourregions = ['LONDON','LEEDS','CARDIFF','BRISTOL']
property_types = ['TERRACED','SEMI-DETATCHED','DETATCHED']

def return_stock():
    print("CURRENT HOUSES FOR SALE \n\n REGION - HOUSE TYPE - BEDROOMS - COST")
    for i in houses:
        print(i)

def unique_regions():
    unique_list = []
    existing_regions = [item[0] for item in houses]
    for x in existing_regions:
        if x not in unique_list: #unique_list -> ourregions
            unique_list.append(x)
    print(unique_list)

def region_search():
    print("Available Regions")
    unique_regions()
    while True:
        region_select = input("Please enter region: ").upper()#capitalize -> upper
        for x in houses:
            if region_select == x[0].upper():
                print(x)
                Valid = True
        if Valid:print("Entered region is not valid")

def show_sales():
    if len(sales) > 0: # sold -> sales
        print("Forename Surname Property cost Total")
        for i in sales:
            forename,surname,propertycost,finalcost = i
            print(f"""==================================
{forename} {surname} 
Property cost: £{propertycost:.2f}
Final cost: £{finalcost:.2f}
==================================""")
    else:print("no sales")
    
def house_sale():
        sale = []
        customer_forename = input("Please enter customer forename.")
        customer_surname = input("Please enter customer surname.")
        for i,item in enumerate(houses, 1):
            print(i,item)
        
        while True:
            try:
                select = int(input("Please select a purchase"))
                if 0 < select < len(houses): # changed
                    break
            except:
                print("ERROR PLEASE ENTER A VALID PROPERTY")
        
        sub_total = houses[select-1][3]
        print(f"£{sub_total:.2f}")
        total_fees = 0
        
        if sub_total > 100000:
            total_fees += 3000 + (sub_total-100000)*0.02 # 0.2 -> 0.02
        else:
            total_fees += sub_total*0.03 # 0.3 -> 0.03

        final_total = sub_total+total_fees
        sale.append(customer_forename)
        sale.append(customer_surname)
        sale.append(sub_total)
        sale.append(final_total)
        sales.append(sale)
        
        print(f'Customer Recipt\n\n {customer_forename} {customer_surname} £{final_total:.2f}')
        print("\nTRANSACTION COMPLETE - PROPERTY REMOVED FROM SALES DATABASE\n")
        del houses[select-1]
        
while True:
    try:
        menuselection = int(input(""" WELCOME TO THE NEWHAVEN DASHBOARD \n\n Please select from the following menu options \n\n 
1: View current houses on market 
2: Search for available houses in a region
3: Record a sale
4: Add a new property for sale
5: Show Sales
6: Exit"""))
        if menuselection == 1:
            return_stock()
        elif menuselection == 2:
            region_search()
        elif menuselection == 3:
            house_sale()
        elif menuselection == 4:
            print("This feature is not yet available we are sorry for the inconvinience.")
        elif menuselection == 5:
            show_sales()
        elif menuselection == 6:
            break
        else:
            print("INVALID SELECTION")
        input()
    except:
        print("INVALID SELECTION")
        input("\n")
#reworked menu