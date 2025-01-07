'''
Murray Watt
mwatt29@uwo.ca
251341261
This code intends to fufill the second part of Assignment 1, using the range function
to complete the task.
'''

# Function to format currency with comma separators
def FormatCurrency(amount):
    return "${:,.2f}".format(amount)

# Print headers 
print("Project Two (02): Magguilli Retirement Fund\n")
NumDays = int(input("Enter Number of Days: "))

# Initialize variables
CurrentAmount = 0.01
AccumulatedAmount = 0.00

# Loop for specified number of days
for day in range(1, NumDays + 1):
    # Print current amount for the day
    print(f"Day  {day}  Current Amount:         {FormatCurrency(CurrentAmount)}")
    
    # Update the accumulated amount
    AccumulatedAmount += CurrentAmount
    
    # Print the current accumulated amount
    print(f"Day  {day}  Current Accumulated:    {FormatCurrency(AccumulatedAmount)}\n")
    
    # Double the current amount for the next day
    CurrentAmount *= 2

# Print final values
print(f"Final Value:                    {FormatCurrency(CurrentAmount / 2)}")
print(f"Total Accumulated:              {FormatCurrency(AccumulatedAmount)}\n")

print("END: Project Two (02)")
