# finance_calculator.py
# Personal Finance Calculator (no conditionals)

# User inputs
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculations
monthly_savings = income - expenses
annual_savings = monthly_savings * 12
projected_annual = annual_savings + (annual_savings * 0.05)  # 5% simple interest on the year's savings

# Outputs
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual:.2f}.")
