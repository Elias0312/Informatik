import random

people = [1, 2, 3, 4, 5, 6]
index = 0
last_index = 0
nop = len(people)
print(people)

while True:
    if nop > 1:
        dice = random.randint(1, 6) 
        index = (index + dice) % nop
        print(f"Person {people[last_index % nop]} rolled {dice} -> person {people[index]} will be removed!")
        last_index = index
        del people[index]
        print(people)
        nop = len(people)
    else:
        break