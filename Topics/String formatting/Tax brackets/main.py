income = int(input())
if income < 15528:
    tax_rate = 0
elif income < 42708:
    tax_rate = 15
elif income < 132407:
    tax_rate = 25
else:
    tax_rate = 28
tax = round(income * tax_rate / 100)
f_out = "The tax for {0} is {1}%. That is {2} dollars!"
print(f_out.format(income, tax_rate, tax))
