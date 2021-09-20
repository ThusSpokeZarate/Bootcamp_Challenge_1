# coding: utf-8
import csv
from pathlib import Path

#Initial loan cost list
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# Print the number of loans from the list
number_of_loans = len(loan_costs)
print(f"A total of {number_of_loans} loans were issued.")


# What is the total of all loans?
# Print the total value of the loans
total_loans_value = sum(loan_costs)
print(f"The total value of the loans is ${total_loans_value}.")

# What is the average loan amount from the list?
# Print the average loan amount
average_loan = total_loans_value / number_of_loans
print(f"The average value per loan is ${average_loan}.")


# Given the following loan data, calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

print(future_value)
print(remaining_months)


# Calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
discount_rate = .2
present_value = future_value / (1 + (discount_rate/12))**remaining_months
print(present_value)

#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!
if present_value >= loan["loan_price"]:
    print("The loan is at least worth the cost to buy")
else:
    print("The loan is too expensive and not worth the price.")


# Given the following loan data, calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
#    include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    return the `present_value` for the loan.

def present_value_calc(future_value, remaining_months, annual_discount_rate):
   present_value = future_value / (1 + (annual_discount_rate/12))**remaining_months
   return present_value




# Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = .2
present_value = present_value_calc(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The present value of the new loan is: {present_value}")


#new data for series of loans to be evaluated

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Append any loan from the list that cost $500 or less to the new list `inexpensive_loans`
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)


# Print the `inexpensive_loans` list
print(inexpensive_loans)

# Export 'inextpensive_loans' list to csv file
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())
