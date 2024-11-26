
# 1)

user_input = int(input("Enter a number: "))
if user_input < 0:
    print("This number is negative")
elif user_input > 0:
    print("This number is positive")
elif user_input == 0:
    print("This number is zero")

# 2)

user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second input: "))
if user_input1 < user_input2:
    print("Second number is bigger")
elif user_input1 > user_input2:
    print("First number is bigger")
elif user_input1 == user_input2:
    print("This is equal")

# 3)

user_input = int(input("Enter a number between 1 to 10: "))
if user_input == 6:
    print("You won 100000$")
elif user_input == 2:
    print("You won 10000$")