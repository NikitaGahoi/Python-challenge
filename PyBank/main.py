#Modules
import os
import csv

# Set path for file
csv_path = os.path.join('.', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csv_path, 'r') as csvfile:
    budget_file = csv.reader(csvfile, delimiter=",")
    header = next(budget_file)

    #create empty list to hold the calculated value
    profit_loss = []
    change_profit = []
    months = []

    #calculate the total months 
    total_months = 0
    total = 0
    max_profit = 0
    min_profit = 0

    # Loop through the data to store in a dictionary
    for row in budget_file:

        #calculate total months
        total_months += 1

        #calculate net total amount of "Profit/Losses" over the entire period
        total = total+ int(row[1])
        total = total

        #add the values of month and profit_loss(as_integer) in a new list
        months.append(row[0])
        profit_loss.append(int(row[1]))

    # Append the list (change_profit) that contain the values of "Profit/Losses" changes over the entire period
    for i in range(total_months-1):
        difference = (profit_loss[i+1]-profit_loss[i])
        change_profit.append(int(difference))

    #Calculte the average of "Profit/Losses" changes
    avg_change = round(sum(change_profit)/len(change_profit),2)

    #Calculte the maximum and minimum profit changes
    max_profit = max(change_profit)
    min_profit = min(change_profit)
    
    #Index the maximum and minimum profit changes, to map it to the month
    for i in range(len(change_profit)):
        if change_profit[i] == max_profit:
            max_index = (i+1)
        elif change_profit[i] == min_profit:
            min_index = (i+1)

#Print results
print("Financial Analysis")
print("-----------------------------------------------------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {months[max_index]} (${max_profit})")
print(f"Greatest Decrease in Profits: {months[min_index]} (${min_profit})")


#create a text file named 'PyBank_analysis.txt' to store the result of analysis. '/n' is used to add the line in the text file
output_file = os.path.join('.', 'Analysis', 'PyBank_analysis.txt')
with open(output_file,"w") as result_file:
    result_file.write("Financial Analysis")
    result_file.write("\n")
    result_file.write("------------------------")
    result_file.write("\n")
    result_file.write(f"Total Months: {total_months}")
    result_file.write("\n")
    result_file.write(f"Total: {total}")
    result_file.write("\n")
    result_file.write(f"Average Change: {avg_change}")
    result_file.write("\n")
    result_file.write(f"Greatest Increase in Profits: {months[max_index]} (${max_profit})")
    result_file.write("\n")
    result_file.write(f"Greatest Decrease in Profits: {months[min_index]} (${min_profit})")
