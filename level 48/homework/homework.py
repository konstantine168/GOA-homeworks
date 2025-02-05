# 1)
import random
def append_int(lst):
    for i in range(50):
            lst.append(i)
# 2)
def func(lst):
    
# 3) ფუნქცია, რომელიც სტრინგში ამატებს შემთხვევით სიმბოლოებს და რიცხვს 1-10-დან
def add_random_symbols():
    symbols = ["#", "*", "%", "&", "@", "!"]
    result = ""
    for i in range(5):  # 5-ჯერ დაამატებს
        result += random.choice(symbols) + str(random.randint(1, 10))
    return result

print(add_random_symbols())

# 4) ფუნქცია, რომელიც სიის ყველა ელემენტს აბრიცხავს და დაბეჭდავს
def square_list(numbers):
    squared_numbers = [num ** 2 for num in numbers]
    print(squared_numbers)

square_list([2, 4, 6, 8, 10])

# 5) ფუნქცია, რომელიც მომხმარებელს სთხოვს 3 საყვარელი სპორტი და შემთხვევით აირჩევს ერთს
def favorite_sport():
    sports = []
    for i in range(3):
        sport = input("მიუთითეთ თქვენი საყვარელი სპორტი: ")
        sports.append(sport)
    return random.choice(sports)

print(favorite_sport())