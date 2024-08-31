print("\033")

def tipcalc(b , tipPerc):
    tp = b * (0.01 * tipPerc)
    return tp

bill = int(input("Enter the bill: "))
tip = int(input("Enter the tip Percentage: "))

total = bill + tipcalc(bill , tip)

print(f"Bill = {bill}")
print(f"tip Percentage: {tip}%")
print(f"Total bill = {total}")
