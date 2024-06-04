height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

Body = round(weight / height ** 2)
if Body < 18.5:
    print(f"Your BMI is {Body}, You are underweight")
elif Body < 25:
    print(f"Your BMI is {Body}, You have a normal weight")
elif Body < 30:
    print(f"Your BMI is {Body}, You are overweight")
elif Body < 35:
    print(f"Your BMI is {Body}, You are obese")
else :
    print(f"Your BMI is {Body}, You are clinically obese")