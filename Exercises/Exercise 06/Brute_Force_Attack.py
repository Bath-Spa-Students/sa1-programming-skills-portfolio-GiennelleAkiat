#===============================================================
#------------------------EXERCISE 6
#===============================================================
'''
## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345.
The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts.
If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
'''


#===============================================================
#------------------------WORK
#===============================================================

#========= Counting amount of trials
count = 0

#========== Looping until 5 attempts ran out
while count < 5:
    password = int(input("Enter a 5 digit password: "))
    if password == 12345:
        print("Correct Password Entered.")
        break
    count += 1
    attempts = 5 - count
    print(f"You have {attempts} remaining attempts.")

