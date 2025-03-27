# 1
def fox_bear(lst):
    return lst.min() and lst.max()
# 2
def turtle_vs_turtle():
    input_1 = int(input("Enter A number: "))
    input_2 = int(input("Enter A number: "))
    if input_1 > input_2:
        return "Turtle 1 Is Faster Than Turtle 2!"
    else:
        return "Turtle 2 Is Faster Than Turtle 1"
# 3
def biggest_number():
    list_input = list(input("Enter A sequence of numbers: "))
    x = list_input.remove(list_input.max())
    return x
# 4
def save_dogo():
    Int_input = list(input("Enter 3 numbers:"))
    x = Int_input.split()
    return x[0] + 10
    return x[1] + 10
    return x[2] + 10
# 5
def life_risk(s):
    if s == "ბატკანია":
        return "გადარჩი"
    elif s != "ბატკანია":
        return "მგელმა შეგჭამა!"