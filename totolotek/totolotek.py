import random


def find_totolotek_victory(my_numbers, draws=0, cash=0):
    totolotek_number = None
    while my_numbers != totolotek_number:
        draws += 1
        cash += 3
        totolotek_number = random.sample(range(1, 20), 6)
    return f"Won after {draws} draws and spent {cash:,}zł"

result = find_totolotek_victory([num for num in range(1,7)])
print(result)


def check_values():
    while True:
        yield random.sample(range(1, 50), 6)


def check_values(numbers, ran = None, step=0, cash=0):
    while numbers != ran:
        step +=1
        cash += 3
        ran = random.sample(range(1, 10), 6)
    return f"Won after {step} draws and spent {cash:,}zł"


def check_values(numbers, step=0, cash=0):
    while numbers:
        number = numbers.index(random.randint(1, 7))
        step +=1
        cash += 3
        if number in numbers:
            numbers.pop(numbers.index(number))
#     return f"Won after {step} draws and spent {cash:,}zł"

for i in check_values():
    print(i == [1,2,3,4,5,6])

print(check_values)

# print(check_values([1,2,3,4,5,6]))
