#User input for financial details
Monthly_income = int(input("Enter your monthly income:"))
Monthly_expenses = int(input("Enter your monthly expenses:"))

#Calculate monthly savings
Monthly_Savings = Monthly_income - Monthly_expenses

#Project annual savings
Simple_interest_rate = 0.05
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

print(f"Your monthly savings are ${Monthly_Savings}")
print("Projected savings after one year, with interest, is: $" + str(int(Projected_Savings))+".")
