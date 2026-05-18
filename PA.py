# Author: Wesley Gavitt
# Student ID: WESGAV9989
# Purpose: Performance Assessment - Basic Python Calculations

name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")

first_number = int(input("Please enter a whole number: "))
second_number = int(input("Please enter a different second whole number: "))

multiplication = first_number * second_number
division = first_number / second_number
subtraction = first_number - second_number

print(f"The result of {first_number} times {second_number} is: {multiplication:.2f}")
print(f"The result of {first_number} divided by {second_number} is: {division:.2f}")
print(f"The result of {first_number} minus {second_number} is: {subtraction:.2f}")

if first_number > second_number:
    print("Number 1 is larger than Number 2")
elif first_number < second_number:
    print("Number 1 is smaller than Number 2")
else:
    print("Number 1 is equal to Number 2")

print(name)
print(student_id)