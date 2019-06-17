
import os
import csv

# Define csv path
budget_csv = os.path.join("budget_data.csv")

# Track total months for output and row counting
total_months = 0

# Create lists to store data
months = []
net_pl = []
changes = []

# open csv
with open(budget_csv, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # skip header row
    next(csvreader)
    
    # loop through csv
    for row in csvreader:
        total_months = total_months + 1
        net_pl.append(int(row[1]))
        prev = total_months - 1
        change = int(row[1]) - net_pl[(prev-1)]
        changes.append(change)
        months.append(str(row[0]))

# define values used in output
total = sum(net_pl)
avg_chg = round(sum(changes)/(len(changes)-1),2)
max_value = max(changes)
min_value = min(changes)
max_index = changes.index(max_value)
min_index = changes.index(min_value)
max_month = months[max_index]
min_month = months[min_index]

# Output of financial analysis
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${avg_chg}')
print(f'Greatest Increase In Profits: {max_month} (${max_value})')
print(f'Greatest Decrease In Profits: {min_month} (${min_value})')


with open("PyBank.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total}', file=text_file)
    print(f'Average Change: ${avg_chg}', file=text_file)
    print(f'Greatest Increase In Profits: {max_month} (${max_value})', file=text_file)
    print(f'Greatest Decrease In Profits: {min_month} (${min_value})', file=text_file)
