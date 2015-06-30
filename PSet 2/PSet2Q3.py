def finalBalance(startBalance, annualInterestRate, monthlyPayment):
    for month in range(12):
        startBalance -= monthlyPayment
        startBalance *= (1 + (annualInterestRate / 12))
    return startBalance
 
accuracy = 0.000001
lower = balance / 12
upper = (balance * ((1 + (annualInterestRate/12)) ** 12)) / 12
payment = 0.5 * (upper + lower)
finalBal = finalBalance(balance, annualInterestRate, payment)
while abs(finalBal) > accuracy:
    if finalBal< 0:
        upper = payment
    else:
        lower = payment
    payment = 0.5 * (upper + lower)
    finalBal = finalBalance(balance, annualInterestRate, payment)
print("Lowest payment: {0:.2f}".format(payment))