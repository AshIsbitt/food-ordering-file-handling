import os

def switchboard():

    if os.path.exists("order.txt"):
        os.remove("order.txt")

    while True:

        print("0. Exit")
        print("1. Enter new food item")
        print("2. See current order")
        print("3. Edit order")
        entry = input("> ")

        try:
            entry = int(entry)
        except ValueError:
            print("Enter new value")
            continue

        if entry == 0:
            quit()
        elif entry == 1:
            add_food_item()
        elif entry == 2:
            print(see_order())
        elif entry == 3:
            rem_item()
        else:
            print("Invalid Entry")

    print("--------------")


def add_food_item():
    print("Enter food item: ")
    entry = input("> ")

    try:
        with open("order.txt", 'a') as file:
            file.write(entry + "\n")

            print(entry + " added to order")
    except FileNotFoundError as e:
        print("Nonexistent file")
        print(e)

    print("-------------")


def see_order():
    count = 0
    print("-----------")
    print("Food order:")

    try:
        with open("order.txt", 'r') as file:
            food_order = file.readlines()

            for item in food_order:
                print(str(count + 1) + ". " + item.rstrip("\n"))
                count += 1

    except FileNotFoundError as e:
        print("Nonexistent file")
        print(e)

    print("-------------")


def rem_item():
    count = 0
    print("-----------")
    food_rem = int(input("Enter the number of the item to remove: ")) - 1


    try:
        with open("order.txt", 'r') as file:
            food_order = file.readlines()

        with open("order.txt", 'w') as file:
            food_order.pop(food_rem)

            for item in food_order:
                file.write(item + "\n")

    except FileNotFoundError as e:
        print("Nonexistent file")
        print(e)



    finally:
        print("-------------")


switchboard()
