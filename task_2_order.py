import os

from newuser import *

file_objects = []

if os.path.exists("order2.txt"):
    os.remove("order2.txt")

try:
    with open("order2.txt", 'a') as file:
        name_list = ["Jack", "Owen", "Ianto", "Gwen", "Toshiko",
                     "Sarah", "Martha", "Rose", "Micky", "Donna"]

        for item in name_list:
            file.write(item+"\n")

    with open("order2.txt", 'r') as file:
        rl = file.readlines()

        for item in rl:
            obj = NewUser(item.rstrip("\n"))
            file_objects.append(obj)
            print(file_objects[-1].get_name())

except FileNotFoundError:
    print("No file")