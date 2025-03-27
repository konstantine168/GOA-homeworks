# 1
def A_B(a, b):
    return a * b
# Usage:
print(A_B(1, 7))
print(A_B(5, 9))
print(A_B(2, 9))
print(A_B(9, 1))
print(A_B(0, 12))
# 2
# def Add_Up(HP):
#     return HP + 10
# def Decrease(HP):
#     return HP - 10
# def main(HP):
#     print(Add_Up(21))
#     print(Decrease(64))
# # Usage:
# print(main())
# 3
def nugzar_chubinidze(sadgerdzelo, limit):
    if limit > sadgerdzelo:
        return "დათვრა"
    else:
        return "მოდი ახლა მართლა, დამილოცნიე!"
# Usage:
print(nugzar_chubinidze(10, 15))
# 4
def stone_throw(shot):
    if shot < 0:
        return "ვაიმე პირდაპირ ფეხში მომხვდა!"
    elif shot > 2:
        return "ვაიმე ორივე ფეხში მომხვდა!!!"
