student_height = input("Input a list of student heights ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print(student_height)

total_height = 0
for height in student_height:
    total_height += height

print(total_height)

number_of_students = len(student_height)
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)
