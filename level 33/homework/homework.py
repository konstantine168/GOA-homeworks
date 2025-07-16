# 1) სახელების გახლეჩვა და მისალმება
names = "ლუკა გიო ნინო ნიკა ლიზი"
names_list = names.split()
for name in names_list:
    print(f"გამარჯობა {name}")
# 2) ტექსტის ჩანაცვლება
sentence1 = "ამინდი ძალიან კარგია დღეს"
sentence2 = "გოგო და ბიჭი ერთად თამაშობენ"
sentence1 = sentence1.replace("ა", "#")
sentence2 = sentence2.replace("გ", "*")
print(sentence1 + " " + sentence2)
# 3) ანდაზის გახლეჩვა და ყველაზე დიდი/პატარა სიტყვის პოვნა
proverb = input("შეიყვანეთ თქვენი საყვარელი ანდაზა: ")
words = proverb.split()
longest_word = max(words, key=len)
shortest_word = min(words, key=len)
print(f"ყველაზე დიდი სიტყვა: {longest_word}")
print(f"ყველაზე პატარა სიტყვა: {shortest_word}")
# 4) space-ების წაშლა replace-ით
text = "i love python == True"
text = text.replace(" ", "")
print(text)
# 5) space-ების წაშლა და ტექსტის შებრუნება
text = "i love html but its not a programming language :'("
text = text.replace(" ", "")[::-1]
print(text)
# 6) სახელების სია და დიდი ასოებით შენახვა
names = ["ლუკა", "გიო", "ნინო", "ნიკა", "ლიზი"]
capital_names = [name.upper() for name in names]
print(capital_names)