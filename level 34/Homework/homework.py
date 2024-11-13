# 1)
def say_hello():
    print("გამარჯობა!")
# output:
say_hello()
print("---------------------------")
# 2)
def sum_two_numbers():
    print(2 + 2)
# output:
sum_two_numbers()
print("---------------------------")
# 3)
user_age = int(input("enter your age:"))
def calculate_age():
    print(f"your age is:{user_age}")
# output:
calculate_age()
print("---------------------------")
# 4)
user_multiplication_1 = int(input("enter the 1st number that you want to multiply:"))
user_multiplication_2 = int(input("enter the 2nd number that you want to multiply:"))
def multiply():
    print(user_multiplication_1 * user_multiplication_2)
# output:
multiply()
print("---------------------------")
# 5)
def repeat():
    user_word_str = str(input("enter the word that you want to be outputed twice:"))
    print(f"{user_word_str * 2}")
# output:
repeat()