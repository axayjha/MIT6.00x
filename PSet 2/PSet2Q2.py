monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance

while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1
    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
        month += 1
    newbalance = round(newbalance,2)
    
print (" Lowest Payment:", monthlyPayment)