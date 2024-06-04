year= int(input("which Year do you want to check? "))
#i wanted to use the solution in the video because i did not get it a first
# but i kept having errors
#that was why i  decided to use the elif expression

if year % 4 == 0:
        print("this is a leap year")
elif year % 100 == 0:
       print("this is a leap year")
elif year % 400 == 0:
       print("this is a leap year")
else:
       print("This is not a leap year")