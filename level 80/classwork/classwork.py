def My_Room(Real):
    Tempeture = 78
    if Real > Tempeture:
        return "უჰ, დავიწვით აქა კაცო დაუწიე!"
    else:
        return "უჰ, რა კაი სიგრილეა!"

def My_Room_Update(Real):
    Tempeture = 78
    if Real > Tempeture:
        return "უჰ, დავიწვით აქა კაცო დაუწიე!"
    elif Real <= 25:
        return "ვიყინები!"
    elif Real <= 50:
        return "ცოტათი, ცოტათი ნორმალურია!"
    elif Real <= 0:
        return "აააააააააააააააა!"
    elif Real <= -25:
        return "მიშველეეეეეეეეეეეეეეეთ!!!"
    elif Real <= -50:
        return "BRUH!"
    else:
        return "უჰ, რა კაი სიგრილეა!"