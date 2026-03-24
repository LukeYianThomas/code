import pandas,matplotlib.pyplot as plt,numpy as np

def show_menu():
    #displays options for the user to choose from
    print("\n"+"="*50)
    print("             CAR SALES MENU")
    print("\n"+"="*50)
    print("""1. General sales details (Sum, Avg, Max, Min)
2. Total sales income by salesperson (Bar Chart)
3. Total sales income by car model (Pie Chart)
4. Search for specific salesperson
5. Search for specific car model records
6. Cumulative frequency of total sales
7. Sales trend by salesperson (Line graph)
8. Sales trend over time (Line graph)
9. Sort total sales by salesperson (A-Z)
10. Sort total sales by value (High to low)
11. Total sales value for used cars
12. Exit""")

def sales_details():
    #displays general information about sales
    print(f"""\nTotal sales: £{df["Value"].sum():,.2f}
Average sales: £{df["Value"].mean():,.2f}
Highest sale: £{df["Value"].max():,.2f}
Lowest sale: £{df["Value"].min():,.2f}""")
    input()

def sales_by_person_summary():
    print("\n--- Sales by Person ---")
    result = df.groupby("Salesperson").agg(
        Cars_Sold = ("Car Model", "count"),
        Total_Value = ("Value", "sum")
    )
    print(result)
    input()
    
    total_sales = df.groupby("Salesperson")["Value"].sum()
    plt.figure(figsize=(10,5))
    plt.bar(total_sales.index,total_sales.values,color="skyblue")
    plt.xlabel("Salesperson")
    plt.ylabel("Total Sales Value (£)")
    plt.title("Total Sales Value for Each Salesperson")
    plt.xticks(rotation=45)
    plt.show()
    input()
    
def cars_by_model_summary():
    print("\n--- Total Sales by Car Model ---")
    result = df.groupby("Car Model")["Value"].sum().reset_index()
    result_display = result.copy()
    result_display["Value"] = result_display["Value"].map('£{:,.2f}'.format)
    print(result_display.to_string(index=False))
    plt.figure(figsize=(8,8))
    plt.pie(
        result["Value"],
        labels=result["Car Model"],
        autopct='%1.1f%%',
        startangle = 140
    )
    plt.title("Total Sales Income by Car Model")
    plt.axis('equal')
    plt.show()
    input()

def search_by_salesperson():
    salesperson = input("Enter the salesperson name to search for:")
    filtered = df[df["Salesperson"].str.lower()==salesperson.lower()]
    if not filtered.empty:
        print(f"\nRecords for salesperson '{salesperson}':")
        print(filtered)
        print(f"\nTotal cars sold: {len(filtered)}")
        print(f"\nTotal sales value: £{filtered['Value'].sum():,.2f}")
    else:
        print(f"\nNo records found for salesperson '{salesperson}'.")
    input()

def search_by_model():
    model = input("Enter the model name to search for:")
    filtered = df[df["Car Model"].str.lower()==model.lower()]
    if not filtered.empty:-
        print(f"\nRecords for model '{model}':")
        print(filtered)
        print(f"\nTotal units sold: {len(filtered)}")
        print(f"\nTotal sales value: £{filtered['Value'].sum():,.2f}")
    else:
        print(f"\nNo records found for salesperson '{model}'.")
    input()

def cumulative_frequency_total_sales():
    #wip
    print("\n--- Cumulative Frequency of Total Sales (Quartiles) ---")
    sorted_values = df["Value"].sort_values()
    cumulative_freq = range(1,len(sorted_values)+1)
    q1 = sorted_values.quantile(0.25)
    q2 = sorted_values.quantile(0.50)
    q3 = sorted_values.quantile(0.75)
    q4 = sorted_values.quantile(1.00)
    plt.hist(sorted_values, bins=30, cumulative=True, histtype='stnpopep', label='Cumulative')
    plt.title('Cumulative Frequency Chart')
    plt.xlabel('Data Values')
    plt.ylabel('Cumulative Frequency')
    plt.grid(True)
    plt.show()
    input()
    
def sales_trend_by_salesperson():  
    input()
    
def sales_trend_by_car_model():
    input()
    
def sort_sales_by_salesperson():
    result = df.groupby("Salesperson")["Value"].sum().reset_index()
    result_display = result.copy()
    result_display["Value"] = result_display["Value"].map('£{:,.2f}'.format)
    print(result_display.to_string(index=False))
    input()

def sort_sales_by_value():
    result = df.groupby("Model")["Value"].sum().reset_index()
    result_display = result.copy()
    result_display["Value"] = result_display["Value"].map('£{:,.2f}'.format)
    print(result_display.to_string(index=False))
    input()

def used_cars_summary():
    input()

def selection(choice):
    #Depending on choice it uses different functions
    if choice == "1":
        sales_details()
    elif choice == "2":
        sales_by_person_summary()
    elif choice == "3":
        cars_by_model_summary()
    elif choice == "4":
        search_by_salesperson()
    elif choice == "5":
        search_by_model()
    elif choice == "6":
        cumulative_frequency_total_sales()
    elif choice == "7":
        sales_trend_by_salesperson()
    elif choice == "8":
        sales_trend_by_car_model()
    elif choice == "9":
        sort_sales_by_salesperson()
    elif choice == "10":
        sort_sales_by_value()
    elif choice == "11":
        used_cars_summary()
    elif choice == "12":
        print("\nExiting program. Goodbye!")
        # to break from the loop from within a function an exception is raised
        raise programDone

class programDone(Exception): pass
df = pandas.read_csv("Task3_data.csv")
while True:
    show_menu()
    selection(input("\nEnter your choice (1-12):"))