fruits_list = ["apple", "banana", "peach"]
fruits_list.append("strawberry")
# # 2)
favourite_films = ["harry potter", "indiana jones", "star wars", "spider-man", "batman"]
favourite_films.pop(4)
# # 3)
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in number_list:
    print(i)
# # 4)
animal_list = []
input1 = input("enter an animal: ")
input2 = input("enter an animal: ")
input3 = input("enter an animal: ")
animal_list.append(input1)
animal_list.append(input2)
animal_list.append(input3)
print(animal_list)
# 5)
name_list = ["nika", "konstantine", "dato"]
for i in name_list:
    print(f"hello {i}")
# 6)
friends_name = ["cotne", "sandro", "andria"]
friends_name.insert(0, "konstantine")
print(friends_name)
# 7)
number_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
number_list.sort()
print(number_list)
# 8)
books_list = ["peppy", "harry poter", "game of thrones", "famous 5", "batman"]
famou5_index = books_list.index("famous 5")
print(famou5_index)
# 9)
cities_list = ["paris", "prague", "qutaisi", "barcelona", "brooklyn"]
print(cities_list[::-1])
# 10)
nums_list = [10, 7, 3, 4, 2]
for i in nums_list:
    print(i * 2)
# 11)
random_list = ["apple", "kiwi", "peach"]
print(random_list)
# 12)
num_list = [5, 8, 10, 9]
print(num_list[0])
# 13)
cities_list = ["prague", "paris", "barcelona", "madrid", "qutaisi"]
print(len(cities_list))
