# 1)
num = int(input("შეიყვანეთ რიცხვი:")) # <-- input

if num == 0:
    print("0-ის ტოლია") 
elif num % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")

nums = [] 

for i in range(10):
    num = int(input(f"შეიქვანეთ რიცხვი"))


results = []


for num in nums:
    if num == 0:
        results.append(0)
    elif num % 2 == 0:
        results.append("ლუწია")
    else:
        results.append("კენტია")


print(results)
print("------------------------------")
# 2)
phones_list = [
       "iphone 1"
       ,
       "nokia"
       ,
       "android"
       ,
       "samsung"
       , 
       "iphone 14"
       , 
       "iphone 15" 
       , 
       "iphone 15 pro"
       ,
       "samsung galaxy S 23"
       ,
       "samsung galaxy S 24"
       ,
       "group 38"
]
print(f"ეს არის ტელეფონების სია{phones_list}")

new = input("რომელი ტელეფონი ქსურთ რომ დაამატოთ ტელეფონების სიაში?:")

indexing = int(input(f"სად ქსურთ რომ დაამატოთ სიაში?{phones_list}(0 - {len(phones_list)})"))
phones_list.insert(indexing.new)

print(f"ახალი სია{phones_list}")
print("------------------------------")
# 3)
numbers = [34, 12, 89, 7, 56, 23, 45, 90, 3, 78]


numbers.remove(min(numbers))


numbers.insert(0, 100)
numbers.append(100)


numbers.sort()


print(numbers)
print("------------------------------")
# 4)
shopping_list = [
    "banana"
    ,
    "apple"
    ,
    "monkey"
    ,
    "shaurma"
]
num_items = int(input("რამდენი ტელეფონის მოდელის დამატება გსურთ სიაში? "))

for i in range(num_items): 
    item = input("შეიტანეთ ტელეფონის მოდელი: ")
    shopping_list.append(item)

print("საყიდლების სია:", shopping_list)
# 5)
movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Pulp Fiction"]

while True:
    action = input("გთხოვთ აირჩიოთ: 'დამატება', 'წაშლა' ან 'quit': ").strip().lower()

    if action == "quit":
        break
    elif action == "დამატება":
        neWmovie = input("შეიტანეთ ახალი ფილმის სახელი: ")
        movies.append(neWmovie)
    elif action == "წაშლა":
        Mtr = input("შეიტანეთ ფილმის სახელი, რომელიც უნდა წაიშალოს: ")
        if Mtr in movies:
            movies.remove(Mtr)
        else:
            print("ეს ფილმი არ არის სიაში.")
    else:
        print("გთხოვთ აირჩიოთ 'დამატება', 'წაშლა' ან 'quit'.")

print("ფილმების საბოლოო სია:", movies)