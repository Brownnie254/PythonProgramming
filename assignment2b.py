# Initialize the constants
TAX_RATE = 0.20
STANDARDDEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numdependents = int(input("Enter the number of dependents: "))
# Compute the income tax
taxableIncome = grossIncome - STANDARDDEDUCTION - DEPENDENT_DEDUCTION * numdependents

incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $ ", incomeTax)