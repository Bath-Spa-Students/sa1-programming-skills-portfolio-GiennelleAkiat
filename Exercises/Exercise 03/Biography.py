#===============================================================
#------------------------EXERCISE 3
#===============================================================
'''
## Exercise 3: Biography - 25 Marks

In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.

### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
'''


#===============================================================
#------------------------VARIABLES
#===============================================================

name = str(input("Enter name: "))
town = str(input("Enter hometown: "))
age = int(input("Enter age (must be a number): "))

#===============================================================
#------------------------BIO
#===============================================================

bio = {
    "Name": name,
    "Hometown": town,
    "Age": age
    }

#===============================================================
#------------------------PRINT
#===============================================================

for key, value in bio.items():
    print(f"{key}: {value}")


#-----------------------old test
# bio = {
#     "Name": "Ben Tennyson",
#     "Hometown": "Bellwood",
#     "Age": 16}

#print(bio)