def bachia_da_mgeli(lst, bunny_name):
    if bunny_name in lst:
        return 'შეგჭამ!'
    elif bunny_name not in lst:
        return 'გაგიშვებ!'
    else:
        return 'ჰმმ ვერაფერს ვერ მივხვდი!!!'
# Usage:
bunny_names = ['გოჩა', 'დეიდა', 'დოდო']
print(bachia_da_mgeli(bunny_names, 'გოჩა'))