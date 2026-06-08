r = int(input("input your rating: "))

if 0 <= r <= 5:
    if r < 1:
        print("super duper bad")
    elif 1 <= r < 2:
        print("maybe in the most desperatemoments of your life")
    elif 2 <= r < 3:
        print("it's ok i guess")
    elif 3 <= r < 4:
        print("pretty solid")
    elif 4 <= r < 5:
        print("excellent")
    elif r == 5:
        print("Outstanding, epic, legendary even!")
else:
    print("number out of range!")