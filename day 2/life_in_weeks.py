age = input("what is your curent age? ")
#converting the string to integer
age_as_int = int(age)

#to get the time frame of life left till 90
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"you have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months " 
print(message)