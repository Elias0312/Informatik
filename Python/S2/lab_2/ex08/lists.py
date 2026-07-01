while True:
    myList = []
    item = input("Input command: ")
    if item == "":
        break
    try:
        if int(item) >= 0:
            if int(item) in myList:
                myList.remove(int(item))
            myList.append(int(item))

    except:
        if item == "*":
            for i in myList:
                myList.append(i)
        elif item == "/":
            myList = [myList.remove(i) for i in myList if myList.index(i) % 2 == 0]
        elif item == "help":
            print("""'' (nothing): ends the program
'(integer of your choice)': Adds it to the list.
'*': Doubles the list.
'/': Eliminates every item on an even index.""")
        else:
            print("invalid command! For a list of commands type 'help'.")
    
    