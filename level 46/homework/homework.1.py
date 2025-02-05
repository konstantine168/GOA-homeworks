import random
# 1)
def animal_random(animal_lst):
    return random.append.choise(animal_lst)
# 2)
def film_random(film_list_item_1, film_list_item_2, film_list_item_3, film_list_item_4):
    return random.append.choise(film_list_item_1)
    return random.append.choise(film_list_item_2)
    return random.append.choise(film_list_item_3)
    return random.append.choise(film_list_item_4)
# 3)
def add_random_name():
    result = ""
    name = "თემო"
    for _ in range(5):  # 5-ჯერ დაამატებს სახელს
        result += random.choice(name)
    return result
# 4) ფუქნცია, რომელიც სიისგან რენდომ ხილს აბრუნებს
def random_fruit():
    fruits = ["ვაშლი", "ბანანი", "სტაფილო", "ატამი"]
    return random.choice(fruits)
# 5) ფუქნცია, რომელიც მომხმარებლისგან იღებს 4 საყვარელ ცხოველს და აბრუნებს ერთ მათგანს შემთხვევით
def favorite_animals():
    animals = []
    for _ in range(4):
        animal = input("შეიყვანეთ თქვენი საყვარელი ცხოველი: ")
        animals.append(animal)
    return random.choice(animals)