# 1) chatGPT used:
# ვქმნით names ცვლადს და ვინახავთ მასში სახელებს
names = "ლუკა გიო ნინო ნიკა ლიზი"

# split() ფუნქციით ვგახლიჩავთ სტრინგს
names_list = names.split()

# for ციკლით ვბეჭდავთ მისალმებას თითოეულ სახელს
for name in names_list:
    print(f"გამარჯობა {name}")
# 2) chatGPT not used:
example_name = "hi my name is gaga gugu"
example_name_2 = "hi my name is aiaiaaai"
x = example_name.replace("g" , "*")
y = example_name_2.replace("a" , "#")
print(x)
print(y)
# 3) chatGPT used:
# ვეკითხებით მომხმარებელს მის საყვარელ ანდაზას
proverb = input("რა არის თქვენი საყვარელი ანდაზა? ")

# ვგახლიჩავთ ანდაზას სიტყვებად და ვინახავთ ახალ ცვლადში words
words = proverb.split()

# ვპოულობთ ყველაზე დიდ და პატარა სიტყვებს
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

# ვბეჭდავთ შედეგს
print(f"ყველაზე დიდი სიტყვაა: {longest_word}")
print(f"ყველაზე პატარა სიტყვაა: {shortest_word}")
# 4) chatGPT not used:
text = "I love python == True"
x = text.replace(" " , "")
print(x)
# 5) w3schools used:
text = "i love html but its not a programming language :'(" [::-1]
x = text.replace(" " , "")
print(f"{x}")
# 6) nothing used, just inteligience;) :
names = "name 1 name 2 name 3"

capital_names = names.upper()

print(capital_names)