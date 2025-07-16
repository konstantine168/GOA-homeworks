# 1
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '//':
        return a // b
# 2
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    elif num % 1 == 0:
        return "odd"
# 3
def welcoming(name):
    return f"Hello {name}!"
# 4
def string_multiplication(string, times):
    return string * times
# 5
def jan_klud_vadam_pushups(pushups):
    for i in range(pushups):
        print(pushups)