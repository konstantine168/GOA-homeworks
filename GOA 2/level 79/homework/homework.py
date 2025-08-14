# 1
def traffic_light(color):
    if color == "red":
        return "stop"
    elif color == "yellow":
        return "get ready"
    elif color == "green":
        return "go"
# 2
def school_system(points):
    if points > 100:
        return "Perfect"
    elif points > 89:
        return "good"
    elif points > 74:
        return "average"
    elif points > 49:
        return "weak"
    else:
        return "fail"
# 3
def parking(time):
    if time == "1:00":
        return "Free!"
    elif time == "1:00-3:00":
        return "5GEL"
    elif time == "3:00-6:00":
        return "10GEL"
    elif time > 6:
        return "20GEL"
# 4
def temperature(temp):
    if temp == "30°C":
        return "Hot"
    elif temp < 30:
        return "Warm"
    elif temp > 20:
        return "little Cold"
    else:
        return "Freezing"
# 5
def vending_machine(drink):
    if drink == "Coffee":
        return "Get Up and Work!"
    elif drink == "Tea":
        return "Relax And Chill Out"
    elif drink == "Water":
        return "Start a Healthy Life!"
    elif drink == "Lemonade":
        return "Refresh your body"
    else:
        return "PICK A DRINK!!!"