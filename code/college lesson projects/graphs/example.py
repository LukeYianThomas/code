# The following line imports the Pandas library.
# "as pd": This is called aliasing. It creates a shorthand "nickname" for the library.
# pandas is the industry standard for handling structured data (like spreadsheets or SQL tables).
# This is the most common import, especially in data science and business analytics.
# Reading Files: Loading .csv or .xlsx files into your program.
# Once imported it can be used to:
# Reading Files: Loading .csv or .xlsx files into your program.
# Cleaning Data: Removing empty rows or fixing formatting errors.
# Analysis: Grouping data (e.g., "Show me total sales per salesperson").
# Math: Performing calculations across thousands of rows instantly.

import pandas as pd

#The following line imports the Matplotlib library.
#It is used to create graphs, charts, and plots.
# Much like using pd for Pandas, the Python community almost universally uses plt for Pyplot.
#It makes the code cleaner and faster to write.
import matplotlib.pyplot as plt

#The "try ... except" block is Python’s way of handling errors
#Instead of the program crashing and showing a scary red error message when something
# goes wrong, you can "catch" the error and tell the program how to respond.

try:
    #This line loads the CSV file
    #df (The DataFrame): This is the variable name where your data will live.
    #In the Python world, df is short for DataFrame
    #Think of a DataFrame as a virtual Excel spreadsheet that Python can read and manipulate at high speed.
    df = pd.read_csv("Task4a_data.csv")
    ## Convert the "Date" column from plain text/strings into actual datetime objects
    # 'dayfirst=True' tells Python the dates are in the DD/MM/YYYY format
    #df["Date"]: This selects the column named "Date" from your DataFrame.
    #pd.to_datetime(...): This is a powerful Pandas function that tries to guess or follow rules
    #to turn text (like "15/01/2024") into a digital timestamp.
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
except FileNotFoundError:
    print("Error: 'Task4a_data.csv' not found. Please check the file path.")
    exit()

# ---------- Functions ----------

def sales_details():
    """Display general sales statistics"""
    
    # Print a header for the report section
    print("\n--- General Sales Details ---")
    
    # ".sum" is a built-in function that calculates the sum of all numbers in the 'Value' column
    # :,.2f adds a comma for thousands and rounds to 2 decimal places
    print(f"Total Sales Value:   £{df['Value'].sum():,.2f}")
    
    # ".mean" calculates the mathematical average (mean) of the 'Value' column
    print(f"Average Sales Value: £{df['Value'].mean():,.2f}")
    
    # ".max" finds the single highest number in the 'Value' column
    print(f"Most Expensive Sale: £{df['Value'].max():,.2f}")
    
    # ".min" finds the single lowest number in the 'Value' column
    print(f"Least Expensive Sale: £{df['Value'].min():,.2f}")


# Define a function to calculate performance metrics for each salesperson
def sales_by_person_summary():
    """Display cars sold and total value per salesperson"""
    
    # Print a section header for the console output
    print("\n--- Sales by Person ---")
    
    # Step 1: Group the data by 'Salesperson' and perform two calculations at once
    # 'count' tells us how many cars were sold; 'sum' adds up the total revenue
    # This 'result' variable now contains exactly 3 columns: 
    # [Salesperson, Cars_Sold, Total_Value]
    result = df.groupby("Salesperson").agg(
        Cars_Sold=("Car Model", "count"),
        Total_Value=("Value", "sum")
    )
    
    # Display the summary table on the screen
    print(result)

    # Step 2: Prepare a simplified version of the data specifically for the chart
    # We create a Series where the index is the Name and the value is the total money
    total_sales = df.groupby("Salesperson")["Value"].sum()
       
    # Step 3: Configure the visual appearance of the graph
    # Set the pop-up window size to 10 inches wide and 5 inches high
    plt.figure(figsize=(10, 5))
    
    # Create a bar chart: Names on the x-axis, totals on the y-axis
    plt.bar(total_sales.index, total_sales.values, color='skyblue')
    
    # Add descriptive labels to the axes
    plt.xlabel("Salesperson")
    plt.ylabel("Total Sales Value (£)")
    
    # Give the chart a clear title
    plt.title("Total Sales Value for Each Salesperson")
    
    # Rotate the names on the x-axis by 45 degrees so they are easier to read
    plt.xticks(rotation=45)
    
    # Render and display the chart window to the user
    plt.show()

    

# Define a function to show sales for each model
def cars_by_model_summary():
    """Display total sales income grouped by car model with pie chart"""
    print("\n--- Total Sales by Car Model ---")
    
    # Group data by "Car Model" and sum up the "Value" for each
    # .reset_index() ensures we have a clean table with two columns: 'Car Model' and 'Value'
    result = df.groupby("Car Model")["Value"].sum().reset_index()

    # --- FORMATTING FOR DISPLAY ---
    # Create a copy so we don't mess up the raw numbers used for the chart later
    result_display = result.copy()
    
    # Format the 'Value' column to include the £ sign, commas, and 2 decimal places
    result_display["Value"] = result_display["Value"].map('£{:,.2f}'.format)
    
    # Print the table without the row numbers (index=False) for a cleaner look
    print(result_display.to_string(index=False))

    # --- PIE CHART VISUALIZATION ---
    # Create a square-shaped figure (8x8) to keep the pie chart circular
    plt.figure(figsize=(8, 8))
    
    plt.pie(
        result["Value"],             # The data values (slices)
        labels=result["Car Model"],  # The names of the cars (labels)
        autopct='%1.1f%%',           # Automatically calculate and display percentages
        startangle=140               # Rotate the start of the pie for better aesthetics
    )
    
    plt.title("Total Sales Income by Car Model")
    
    # Ensure the pie is drawn as a circle and not an oval
    plt.axis('equal') 
    
    # Display the chart window
    plt.show()

def search_by_model():
    """Search and display specific records for a car model"""
    # Prompt the user for a string and store it in the variable 'model'
    model = input("Enter the car model to search for: ")
    
    # Create a new DataFrame 'filtered' by comparing lowercase versions of the 
    # 'Car Model' column and the user input to ensure the search is case-insensitive
    filtered = df[df["Car Model"].str.lower() == model.lower()]
    
    # Check if the 'filtered' DataFrame contains any rows (True if results were found)
    if not filtered.empty:
        # Print a header showing which model is being displayed
        print(f"\nRecords for model '{model}':")
        
        # Display the actual rows of data that matched the search
        print(filtered)
        
        # Calculate and print the number of rows found using the len() function
        print(f"\nTotal units sold: {len(filtered)}")
        
        # Sum the 'Value' column and format it with a £ sign, thousands separator, and 2 decimals
        print(f"Total value:      £{filtered['Value'].sum():,.2f}")
        
    else:
        # If the DataFrame was empty, inform the user that no matches were found
        print(f"\nNo records found for model '{model}'.")

def search_by_salesperson():
    # A docstring used to describe the function's purpose for documentation
    """Search and display sales details for a specific salesperson"""
    
    # Prompts the user to enter a name and stores that text in the 'salesperson' variable
    salesperson = input("Enter the salesperson name to search for: ")
    
    # Creates a 'filtered' DataFrame by checking the 'Salesperson' column against the input.
    # .str.lower() and .lower() make the search case-insensitive (e.g., 'JOE' matches 'joe').
    filtered = df[df["Salesperson"].str.lower() == salesperson.lower()]

    # Checks if 'filtered' contains any data; .empty is True if no matches were found
    if not filtered.empty:
        # Displays a header confirming which salesperson's records are being shown
        print(f"\nRecords for salesperson '{salesperson}':")
        
        # Prints the actual rows from the DataFrame that match the salesperson's name
        print(filtered)
        
        # Uses len() to count the number of rows, representing the count of cars sold
        print(f"\nTotal cars sold:  {len(filtered)}")
        
        # Sums the 'Value' column and formats it as currency with commas and 2 decimal places
        print(f"Total sales value: £{filtered['Value'].sum():,.2f}")
        
    else:
        # Executes if the filter returned no rows, informing the user the name wasn't found
        print(f"\nNo records found for salesperson '{salesperson}'.")

def cumulative_frequency_total_sales():
    """Draw cumulative frequency of total sales with quartiles"""
    # Prints a header to the console to let the user know the chart is being generated
    print("\n--- Cumulative Frequency of Total Sales (Quartiles) ---")
    
    # Extracts the 'Value' column and sorts it from lowest to highest (necessary for cumulative charts)
    sorted_values = df["Value"].sort_values()
    
    # Creates a sequence of numbers from 1 up to the total count of sales for the Y-axis
    cumulative_freq = range(1, len(sorted_values) + 1)

    # Calculates the 1st Quartile (the value below which 25% of the data falls)
    q1 = sorted_values.quantile(0.25)
    
    # Calculates the 2nd Quartile or Median (the middle value of the data)
    q2 = sorted_values.quantile(0.50)
    
    # Calculates the 3rd Quartile (the value below which 75% of the data falls)
    q3 = sorted_values.quantile(0.75)

    # Sets up the plotting area with a specific width (9 inches) and height (6 inches)
    plt.figure(figsize=(9, 6))
    
    # Plots the sorted sales on the X-axis and their rank/count on the Y-axis with a green line
    plt.plot(sorted_values, cumulative_freq, marker='o', linestyle='-', color='green')
    
    # Draws a vertical dashed red line at the Q1 value and adds it to the legend
    plt.axvline(q1, color='r', linestyle='--', label=f"Q1 (£{q1:,.0f})")
    
    # Draws a vertical dashed green line at the Median (Q2) value and adds it to the legend
    plt.axvline(q2, color='g', linestyle='--', label=f"Q2 / Median (£{q2:,.0f})")
    
    # Draws a vertical dashed blue line at the Q3 value and adds it to the legend
    plt.axvline(q3, color='b', linestyle='--', label=f"Q3 (£{q3:,.0f})")

    # Labels the X-axis as 'Sales Value' to provide context for the numbers
    plt.xlabel("Sales Value (£)")
    
    # Labels the Y-axis as 'Cumulative Frequency' to show the running total of sales events
    plt.ylabel("Cumulative Frequency")
    
    # Sets the main title for the chart window
    plt.title("Cumulative Frequency of Total Sales")
    
    # Displays the legend (the labels for Q1, Q2, and Q3) on the chart
    plt.legend()
    
    # Adds a background grid to the plot to make reading specific values easier
    plt.grid(True)
    
    # Renders the final plot and displays it in a window
    plt.show()

def sales_trend_by_salesperson():
    """Show line graph of each salesperson's total sales over time"""
    
    # Prints a section header to the console for the user
    print("\n--- Sales Trend by Salesperson Over Time ---")
    
    # Groups data by Date and Salesperson, then sums the 'Value' column.
    # .reset_index() turns the grouped data back into a standard table (DataFrame).
    grouped = df.groupby(["Date", "Salesperson"])["Value"].sum().reset_index()
    
    # Sorts the new DataFrame by 'Date' to ensure the lines draw chronologically left-to-right
    grouped = grouped.sort_values("Date")

    # Initializes the plot window with a width of 12 and height of 6 inches
    plt.figure(figsize=(12, 6))
    
    # Loops through every unique salesperson name found in the grouped data
    for salesperson in grouped["Salesperson"].unique():
        # Creates a temporary subset containing only the rows for the current salesperson in the loop
        data = grouped[grouped["Salesperson"] == salesperson]
        
        # Draws a line for this salesperson, using 'Date' for X and 'Value' for Y, with circular markers
        plt.plot(data["Date"], data["Value"], marker='o', label=salesperson)

    # Sets the label for the horizontal axis
    plt.xlabel("Date")
    
    # Sets the label for the vertical axis, specifying British Pounds (£)
    plt.ylabel("Total Sales Value (£)")
    
    # Adds a descriptive title to the top of the chart
    plt.title("Sales Trend by Salesperson Over Time")
    
    # Places the legend outside the main plot area so it doesn't overlap the lines
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Enables the background grid to make it easier to trace values to the axes
    plt.grid(True)
    
    # Automatically adjusts the plot elements to ensure labels and legends aren't cut off
    plt.tight_layout()
    
    # Renders the window and displays the finished graph
    plt.show()

def sales_trend_by_car_model():
    """Show line graph of each car model's total sales over time"""
    # Prints a section header to the terminal for the user
    print("\n--- Sales Trend by Car Model Over Time ---")

    # Converts the 'Date' column to actual Python datetime objects to ensure 
    # the chart plots chronologically rather than alphabetically
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    # Groups the data by Date and Car Model, sums the values for each group,
    # resets the index to keep it as a table, and sorts it by time
    grouped = (
        df.groupby(["Date", "Car Model"])["Value"]
        .sum()
        .reset_index()
        .sort_values("Date")
    )

    # Creates the plotting window with a width of 12 inches and height of 6 inches
    plt.figure(figsize=(12, 6))

    # Loops through every unique car model name found in the grouped dataset
    for model in grouped["Car Model"].unique():
        # Filters the grouped data to extract only rows belonging to the current model
        model_data = grouped[grouped["Car Model"] == model]
        
        # Plots a line for this specific model, using square ('s') markers for data points
        plt.plot(model_data["Date"], model_data["Value"], marker='s', label=model)

    # Sets the text for the horizontal X-axis (time)
    plt.xlabel("Date")
    
    # Sets the text for the vertical Y-axis (revenue in pounds)
    plt.ylabel("Total Sales Value (£)")
    
    # Adds a main heading to the top of the chart
    plt.title("Sales Trend by Car Model Over Time")
    
    # Adds a legend outside the graph area (loc='upper left' at 1.05) so it doesn't cover the data
    plt.legend(title="Car Models", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adds a dashed background grid with 70% transparency (alpha) to help read values
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Adjusts padding to make sure the legend and axis labels fit within the image file
    plt.tight_layout()
    
    # Displays the final interactive chart window
    plt.show()

def sort_sales_by_salesperson():
    # Docstring explaining that the function summarizes sales and sorts them by name
    """Display total sales value sorted alphabetically"""
    
    # Prints a header to the console so the user knows what they are looking at
    print("\n--- Total Sales Sorted by Salesperson (A–Z) ---")
    
    # Groups the data by "Salesperson" and calculates the sum of the "Value" column for each.
    # .reset_index() converts the result from a Series back into a clean DataFrame table.
    result = df.groupby("Salesperson")["Value"].sum().reset_index()
    
    # Sorts the resulting table alphabetically based on the names in the "Salesperson" column
    result = result.sort_values(by="Salesperson")
    
    # Formats the "Value" numbers into strings with a £ sign, comma separators, and 2 decimals
    # For example: 12500.5 becomes £12,500.50
    result["Value"] = result["Value"].map('£{:,.2f}'.format)
    
    # Prints the final table to the console, hiding the row index numbers for a cleaner look
    print(result.to_string(index=False))

def sort_sales_by_value(descending=True):
    # Docstring explaining that the function summarizes sales and sorts them by the total amount
    """Display total sales value sorted by value"""
    
    # Prints a clear header to the console to inform the user of the output type
    print("\n--- Total Sales Sorted by Value ---")
    
    # Groups the DataFrame by salesperson and totals their sales values.
    # .reset_index() ensures the result is a standard DataFrame with columns "Salesperson" and "Value".
    result = df.groupby("Salesperson")["Value"].sum().reset_index()
    
    # Sorts the table based on the 'Value' column. 
    # 'ascending=not descending' means if descending is True (default), it sorts highest-to-lowest.
    result = result.sort_values(by="Value", ascending=not descending)
    
    # Converts the numerical values into formatted strings with a £ sign, commas, and 2 decimal places.
    # Note: After this step, the 'Value' column is text and can no longer be used for math.
    result["Value"] = result["Value"].map('£{:,.2f}'.format)
    
    # Outputs the final table to the console, removing the row numbers (index) for a cleaner report.
    print(result.to_string(index=False))

def used_cars_summary():
    # Docstring explaining that the function filters and summarizes data for pre-owned vehicles
    """Display list of Used cars and their total"""
    
    # Prints a section header to the console for the user
    print("\n--- Used Cars Summary ---")
    
    # Creates a filtered DataFrame containing only rows where the "New/Used" column is "used".
    # .str.strip() removes accidental spaces, and .str.lower() ensures it matches regardless of casing.
    used_cars = df[df["New/Used"].str.strip().str.lower() == "used"]

    # Checks if the resulting 'used_cars' DataFrame is empty (no matches found)
    if used_cars.empty:
        # Informs the user no data exists for this category and exits the function early
        print("No used cars found.")
        return

    # Prints the full table of records for all cars identified as "used"
    print(used_cars)
    
    # Uses len() to count the rows in the filtered data to show the quantity of cars sold
    print(f"\nTotal used cars sold: {len(used_cars)}")
    
    # Sums the 'Value' column of the filtered data and formats it with £, commas, and 2 decimal places
    print(f"Total value of used cars: £{used_cars['Value'].sum():,.2f}")

def show_menu():
    #"\n" creates a blank line
    # "="*30 tell Python to repeat the character "=" exactly 30 times.
    print("\n" + "="*30)
    print("      CAR SALES MENU")
    print("="*30)
    print("1.  General sales details (Sum, Avg, Max, Min)")
    print("2.  Total sales income by salesperson (Bar Chart)")
    print("3.  Total sales income by car model (Pie Chart)")
    print("4.  Search for specific salesperson")
    print("5.  Search for specific car model records")
    print("6.  Cumulative frequency of total sales")
    print("7.  Sales trend by salesperson (Line Graph)")
    print("8.  Sales trend over time (Line Graph)")    
    print("9.  Sort total sales by salesperson (A–Z)")
    print("10. Sort total sales by value (High to Low)")
    print("11. Total sales value for used cars")
    print("12. Exit")

# ---------- Main Program ----------

# Start an infinite loop to keep the program running until the user chooses to exit
while True:
    # Display the list of available options/actions to the user
    show_menu()
    
    # Capture the user's input and store it in the 'choice' variable
    choice = input("\nEnter your choice (1-11): ")

    # --- INPUT HANDLING LOGIC ---
    # Each 'elif' checks the user's input and calls the corresponding function
    
    if choice == "1":
        sales_details()               # Display raw sales data
    elif choice == "2":
        sales_by_person_summary()      # Show performance totals per salesperson
    elif choice == "3":
        cars_by_model_summary()       # Show how many of each car model were sold
    elif choice == "4":
        search_by_salesperson()       # Filter data for a specific employee
    elif choice == "5":
        search_by_model()             # Filter data for a specific car model
    elif choice == "6":
        cumulative_frequency_total_sales() # Show running totals of sales revenue
    elif choice == "7":
        sales_trend_by_salesperson()  # Visualize/analyze performance over time
    elif choice == "8":
        sales_trend_by_car_model()    # Analyze which models are trending up or down
    elif choice == "9":
        sort_sales_by_salesperson()   # Organize data alphabetically by name
    elif choice == "10":
        sort_sales_by_value()         # Organize data from highest to lowest price
    elif choice == "11":
        used_cars_summary()           # Specifically analyze pre-owned inventory
        
    # --- EXIT CONDITION ---
    elif choice == "12":
        print("Exiting program. Goodbye!")
        break                         # Break ends the 'while True' loop and closes the app
        
    # --- ERROR HANDLING ---
    else:
        # If the user enters anything other than "1" through "12"
        print("Invalid choice. Please enter a number between 1 and 11.")