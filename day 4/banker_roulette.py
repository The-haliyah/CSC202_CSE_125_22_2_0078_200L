names_string = input ("Give me everyone's name, seperated by a comma ")
names = names_string.split(", ")

#get the number of names
num_items = (len(names))
import random
random_choice = random.randint(0, num_items-1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + "is going to buy the meal today")




