# 1
def bunny_hunter(lst, bunny_name):
    if bunny_name in lst:
        return "მგელმა ბაჭია შეჭამა!"
    else:
        return "მგელმა ბაჭია გაუშვა!"
# 2
def eagle_perfume():
    perfume_1 = str(input("რა სუნამოს ისხამ?: "))
    perfume_2 = str(input("რა სუნამოს ისხამ?: "))
    if perfume_1 == perfume_2:
        return "ყოჩაღ გამოიცანი შენ ნამდვილი არწვი ხარ!"
    else:
        return "შე არწივის მატყუარა!"
# 3
def cat_mouse(lst):
    x = lst.split()
    x /= x
    return x