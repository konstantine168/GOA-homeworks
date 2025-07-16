# 1)
def calculate_sum():
    user_input1 = int(input("enter 1st num:"))
    user_input2 = int(input("enter your 2nd num:"))
    print(user_input1 + user_input2)
calculate_sum()
# 2)
def is_even():
    user_input_even_or_odd = int(input("enter a num:"))
    if user_input_even_or_odd % 2:
        print("შენი რიცხვი არის კენტი!")
    else:
        print("შენი რიცხვი არის ლუწი!")
is_even()
# 3)
def greet_user():
    user_name = str(input("რა გქვია?:"))
    print(f"გამარჯობა {user_name}! როგორ ხარ?")
greet_user()
# 4)
def calculate_user_inputs():
    user_num_calculation1 = int(input("enter the 1st num:"))
    user_num_calculation2 = int(input("enter the 2st num:"))
    print(user_num_calculation1 + user_num_calculation2)
calculate_user_inputs()
# 5)
def ეტაპები():
    user_num = int(input("ჩაწერე რიცხვი:"))
    if user_num > 5:
        print("შენ გადახვედი შემდეგ ეტაპზე!")
    else:
        print("შენ არ! გადახვედი შემდეგ ეტაპზე!")
ეტაპები()