#===============================================================
#------------------------LIST
#===============================================================

list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

                        #USER INPUT

user_input = input("Search for a name: ")
user_input = user_input.capitalize()

#===============================================================
#------------------------REPEAT PROCESS
#===============================================================
while user_input not in list:
    print(f"{user_input} is not present in the list")
    user_input = input("Search for a name: ")
    user_input = user_input.capitalize()

    if user_input in list:
        print(f"{user_input} is present in the list.")
        break
