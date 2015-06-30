month=1
paid=0
while month<13:
    print("Month: " +str(month))
    minimumPayment=balance*monthlyPaymentRate
    unpaidBalance=balance-minimumPayment
    interest=(annualInterestRate/12)*unpaidBalance
    balance1=balance-minimumPayment+interest
    print("Minimum monthly payment: " + str(round(minimumPayment, 2)))    
    p1=minimumPayment
    balance=balance-minimumPayment+interest
    print("Remaining balance: " + str(round(balance, 2)))
    month=month+1
    paid=paid+minimumPayment

print("Total paid: "+ str(round(paid,2)))
print("Remaining balance: " + str(round(balance, 2)))

