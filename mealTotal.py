foodCost = float(input("Please enter the cost of the food: "))

tip = foodCost * .18
formatted_tip= "${:,.2f}".format(tip)
print("18 Percent tip: " + formatted_tip)

tax = foodCost * .07
formatted_tax= "${:,.2f}".format(tax)
print("7 Percent tax: " + formatted_tax)

total = foodCost + tip + tax
formatted_total= "${:,.2f}".format(total)

print("The total amount is " + formatted_total)