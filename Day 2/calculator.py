print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? €"))

tip = int(input("How much tip would you like to give? 10, 12 or 15?"))

people = int(input("How many people to split the bill?"))

TipAsPorcent= tip / 100
TotalTipAmount = bill * TipAsPorcent
TotalBill = bill + TotalTipAmount
BillPerPerson = TotalBill / people
FinalAmount = round(BillPerPerson, 2)

print(f"Each person should pay {FinalAmount}")