# 1
def highest_N_lowest(lst):
    x = lst.split()
    return x.max() and x.min()
# 2
def turtle_race():
    turtle_1 = int(input("Input Speed: "))
    turtle_2 = int(input("Input Speed: "))
    if turtle_1 > turtle_2:
        return "Turtle 1 Won!"
    else:
        return "Turtle 2 Won!"
# 3
def skup_skup(lst):
    x = lst.split()
    y = x - x.max()
    return y
# 4
def plussers(lst):
    x = lst.split()
    return x + 10
# 5
def sheep(word):
    if word == "sheep":
        return "Survived!"
    else:
        return "DEAD!"