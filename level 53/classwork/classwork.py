# CW:
# 1)
BMW = {
    "Name": "BMW",
    "Year": 1923
}
BMW["Color"] = "Blue"
BMW["Users"] = 2832415
BMW["Capacity"] = "242KG"
BMW.setdefault("Active Users", 123585) 
print(BMW)
print(BMW["Capacity"])
print(BMW.get("Year", "Name"))
# 2)
favorite_foods = {
    "junk_food": ["Shaurma", "Burger", "Fries"],
    "normal_with_bief": ["Chicken", "Mcroll"]
}