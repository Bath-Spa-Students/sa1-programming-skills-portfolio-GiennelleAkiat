#===============================================================
#------------------------EXERCISE 8
#===============================================================
'''
## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings.
The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
'''


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
