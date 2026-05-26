# Wesley Gavitt
# 5/26/2026
# This program demonstrates functions, parameters, return values, and basic decision logic.

def functionOne():
    print("My Student ID is WESGAV9989")


def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))

    total = num1 + num2

    print(f"The sum of {num1} and {num2} is {total}.")

    return total


def functionThree(total):
    if total > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")

    return 9989


def main():
    # Call functionOne to display the student ID.
    functionOne()

    # Call functionTwo and store the returned sum.
    sumTotal = functionTwo()

    # Call functionThree using the sum and store the returned student ID number.
    studentNumber = functionThree(sumTotal)

    # Display the value returned from functionThree.
    print(f"functionThree returned the value of {studentNumber}.")


main()
