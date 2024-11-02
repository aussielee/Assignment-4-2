# Prompt user for employee's name
employee_name = input("Enter Employee Name: ")

# Prompt user for number of shifts and convert to integer
number_of_shifts = int(input("Enter number of shifts: "))

# Prompt user for number of transactions and convert to integer
number_of_transactions = int(input("Enter number of transactions: "))

# Prompt user for total transaction dollar value and convert to float
transaction_dollar_value = float(input("Enter transactions dollar value: "))

# Calculate productivity score
# Formula: (transaction dollar value / number of transactions) / number of shifts
productivity_score = (transaction_dollar_value / number_of_transactions) / number_of_shifts

# Determine bonus based on productivity score using nested if statements
if productivity_score <= 30:
    # If score is 30 or less, bonus is $50
    bonus = 50.00
else:
    if productivity_score <= 69:
        # If score is between 31 and 69, bonus is $75
        bonus = 75.00
    else:
        if productivity_score <= 199:
            # If score is between 70 and 199, bonus is $100
            bonus = 100.00
        else:
            # If score is 200 or more, bonus is $200
            bonus = 200.00

# Output the employee's name and calculated bonus
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus}")
