# 1)
import random
def random_movie():
    list = ["home alone", "dragonguardian", "Interstellar"] # ეს არის ორიგინალური სია
    list_of_advrand_mov = ["home alone 2", "home alone 3", "home alone fish", "მამლუქი", "ჰარი პოტერი", "წუნა და წრუწუნა"] # ეს არის ის სია რომელი სიიდანაც ელემენტი გადმოვა ორიგინალში
    for i in range(4): # ეს არის for loop. for loop ით გადავუვლით ამ სიას და დავამატებთ list_of_advrand_mov-იდან
        random_item = random.choise(list_of_advrand_mov) # ეს აარჩევს რანდომ ფილმს
        list.append(random_item) # ეს ჩაამატებს ორიგინალში list_of_advrand_mov-ის ელემენტს
        list_of_advrand_mov.remove(random_item) # ეს წაშლის ზედმეტ რანდომ ელემენტს
        return list # ეს გამოიძახებს ლისტს
# Usage:
print(random_movie)
# 2)
def random_name():
    empty_string = "" # ეს არის ცარიელი სტრინგი რაც ამყარებს ამოცანის მეორე პირობას
    my_name = "K o n s t a n t i n e" # <-- ჩემი სახელი 
    my_name_split = my_name.split() # "[K], [o], [n], [s], [t], [a], [n], [t], [i], [n], [e]"
    for char in my_name_split: # for loop name-ის char-ების დასაბეჭდად
        random_char = random.choise(my_name_split) # აარჩევს ჩემი სახელიდან char-ებს
        empty_string += random_char # ჩემ სახელს უმატებს რანდომ char-ს
        my_name_split.remove(random_char) # ამოშლის რანდომ char-ს ჩემი სახელიდან.
    return empty_string # ცარიელი სტრინგი შემოაბრუნე
print(random_name())