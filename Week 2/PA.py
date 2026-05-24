# Wesley Gavitt
# WESGAV9989
# 2.7 Performance Assessment
# This program asks the user to guess a predetermined number,
# then displays results using if/else statements, a while loop, and a for loop.

name = input("What is your name? ")
student_id = input("What is your studentID? ")

print(f"Hello, {name}!")

correct_number = 5
guess_count = 0
guessed_correctly = False

guess = int(input("Please guess a number between 1 and 10..."))
guess_count += 1

if guess < correct_number:
    print("You guessed too low")
elif guess > correct_number:
    print("You guessed too high")
else:
    print(f"Congratulations, {name}! You guessed the number in {guess_count} tries!")
    guessed_correctly = True

while guessed_correctly == False:
    guess = int(input("Please guess a number between 1 and 10..."))
    guess_count += 1

    if guess < correct_number:
        print("You guessed too low")
    elif guess > correct_number:
        print("You guessed too high")
    else:
        print(f"Congratulations, {name}! You guessed the number in {guess_count} tries!")
        guessed_correctly = True

print()
print("Output from the 'while' loop:")

counter = 1
while counter <= 5:
    incremented_number = correct_number + counter
    print(f"{correct_number} incremented by {counter} is {incremented_number}")
    counter += 1

print()
print("Output from the 'for' loop:")

for counter in range(1, 6):
    incremented_number = correct_number + counter
    print(f"{correct_number} incremented by {counter} is {incremented_number}")
