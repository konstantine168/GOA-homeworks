def eagle_eagle():
    type_of_1 = str(input("What type of parfume do you use?: "))
    type_of_2 = str(input("What type of parfume do you use?: "))
    if type_of_1 == type_of_2:
        return "you're an eagle!"
    else:
        return "You ain't! little liar!"
print(eagle_eagle())