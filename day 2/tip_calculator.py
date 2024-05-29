print("welcome to the tip calculator!")
bill = float(input("what was your total bill? $"))
tip= int(input("How tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

#calculaing the bill with the tip
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip /people

#rounding the tip to 2 dp
final_amount = round(bill_per_person, 2)
#making the bill to be definite in giving us 2dp
final_amount = "{:.2f}".format(bill_per_person)

#printing the final result
print(f"Each person should pay: ${final_amount} ")