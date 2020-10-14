import os
import csv

# List to store the month and year 
month = []
# List to store a count to the number of months
month_count = []
# List to store the profit/loss changes calculated in each loop
profit_change_sum = []
# Retrieve the value of each months profit/loss from the csv file
monthly_profit = 0
# Create a variable to store the profit value of the previous loop and in the future calculate profit/loss changes
last_profit = 0
# Create a variable to register the add up of monthly profits
total_profit = 0

budget_file = os.path.join("..","C:analysis/","C:/Users/user/python_demo/python-challenge/PyBank/Resources/","c:/Users/user/python_demo/python-challenge/PyBank/Resources/budget_data.csv")
analysis = "C:analysis/financial_analysis.csv"

# Open csv file and skip header
with open(budget_file,"r") as budget_data:
    budget_reader = csv.reader(budget_data, delimiter=",")
    budget_header = next(budget_reader)
    
    
    for row in budget_reader:
        # adding up to month list we move through the loop
        month.append(row[0])
        # Store variable with total month value
        month_count = len(month)
        # Assign variable to retrieve profit/loss value in each row
        monthly_profit = float(row[1])  
        # Assign a variable to store total profits
        total_profit = monthly_profit + total_profit
        
        # establish the variable to store profit changes
        profit_change = float(monthly_profit - last_profit)
        # Create list to store profit changes
        profit_change_sum.append(profit_change)
        # Reset last profit to the current monthly profit at the end of the loop
        last_profit = monthly_profit
        
    # find max and min values in the list that stores profit changes
    highest_profit_change = max(profit_change_sum)
    lowest_profit_change = min(profit_change_sum)      
    # find the correspondent month to both max and min values of profit monthly changes
    highest_profit_month = month[profit_change_sum.index(highest_profit_change)]
    lowest_profit_month = month[profit_change_sum.index(lowest_profit_change)]
    # Calculate the average profit change by using the sum and lenth of the list of changes
    average_profit_change = round(sum(profit_change_sum)/ len(profit_change_sum),2)

 # print data retrieved
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_profit_change}")
print(f"Greatest increase in profits: {highest_profit_month} $ {highest_profit_change}")
print(f"Greatest decrease in profits: {lowest_profit_month} $ {lowest_profit_change}")

 # Print Text in the output file "financial_analysis"
with open(analysis, "w") as financial_analysis:
    financial_analysis.write("Financial Analysis\n")
    financial_analysis.write("-----------------------\n")
    financial_analysis.write(f"Total Months: {month_count}\n")
    financial_analysis.write(f"Total: ${total_profit}\n")
    financial_analysis.write(f"Average Change: ${average_profit_change}\n")
    financial_analysis.write(f"Greatest increase in profits: {highest_profit_month} $ {highest_profit_change}\n")
    financial_analysis.write(f"Greatest decrease in profits: {lowest_profit_month} $ {lowest_profit_change}\n")


