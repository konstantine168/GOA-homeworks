# 1
def print_numbers(n):
    for დდ in range(n):
        print("ახალი ხაზი")
        print(დდ)
        print("ხაზი დასრულდა")
# Usage:
print_numbers(52)
print_numbers(17)
print_numbers(12)
print_numbers(42)
print_numbers(87)
print_numbers(10)
# 2
def counter(arr):
    counter = 0
    for i in range(arr):
        print("ხაზის დასაწყისი")
        print(i, "+", counter, "=", i + counter, "counter:", i + counter,"-------", "i:", i)
        counter =  i + counter
        print("ხაზის დასასრული")
    return counter
print(counter([1, 2, 3, 4]))
# 3
