# 1)
family_tuple = ("ნინო", "გიორგი", "პელაგია", "კონსტანტინე")
# Result:
print(family_tuple)
# 2)
Charms_Cuphead = ("+1 Health", "Smoke Bomb", "Astral Cookie", "Random Charm", "Random Charm", "Random Charm", "Random Charm", "Random Charm", "Random Charm", "Random Charm",)
charm_1, charm_2, charm_3, *random_charms = Charms_Cuphead
# Result:
print(Charms_Cuphead)
# 3)
tuple_for_chicken = ("Mixed")
chickens = (tuple_for_chicken, "Black", "White")
# Result:
print(chickens)
# 4)
lights = ("bright", "slight-bright")
cities = ("New York", "Tbilisi")
mixed_dict = {
    "Lighting": lights,
    "Cities_(with_tuple)": cities 
}
# Output (Needed_Result):
print(cities[0])
# 5)
musheroom_dict = {
    1: "ქამა",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
    "შემთხევითი": "შემთხვე.სოკ",
}
num_1, *შემთხვევით = musheroom_dict
# Result:
print(musheroom_dict)