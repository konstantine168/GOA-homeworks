# 1)
def forloop_stuff():
    variable1 = 12
    variable2 = 15
    variable3 = 19
    variable4 = 24
    variable5 = 39
    for i in range(variable1):
        print("Hello, World!") # გამოიტანს Hello, World!-ს 12-ჯერ
    for i in range(variable2):
        print("Hello, World") # გამოიტანს Hello, World!-ს 15-ჯერ
    for i in range(variable3):
        print("Hello, World!") # გამოიტანს Hello, World!-ს 19-ჯერ
    for i in range(variable4):
        print("Hello, World") # გამოიტანს Hello, World!-ს 24-ჯერ
    for i in range(variable5):
        print("Hello, World") # გამოიტანს Hello, World!-ს 39-ჯერ
# 2)
def whileloop_stuff():
    question_1 = int(input("15 * 2?: "))
    if question_1 == 30:
        return "Good, Job!"
    else:
        while True:
            return "YOU FAILURE!!!" # თუ არასწორად უპასუხე უსასრულოდ გამოგიტანს YOU FAILURE-ს!
    question_2 = int(input("16 * 2?: "))
    if question_2 == 32:
        while True:
            return "YOU PASSED!" # თუ სწორად გაქვს პასუხი მაშინ დაუმთავრებლად გამოგიტანს YOU PASSED-ს!
    else:
        return "You, Should be ashamed!" # არასწორად და! You, Should be ashamed!
    while True:
        return "Hallo!" # უსასრულო გამარჯობა!
    while 123 == 123:
        return "Hallo!" # იგივე მაგრამ გრძელი გზით (ამ გზას ვიყენებდი ადრე)
    while False:
        return "Nothing at all!" # უბრალოდ არაფერი...FALSE!
# 3) already done :)