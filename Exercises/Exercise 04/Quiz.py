#===============================================================
#------------------------EXERCISE 4
#===============================================================
'''
## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
'''

#===============================================================
#------------------------QUESTION 1
#===============================================================

france = input("1. What is the captial of France? ")
france = france.upper()
if france == "PARIS":
    print("That is correct!")
else:
    print("The correct answer is Paris.")

#===============================================================
#------------------------QUESTION 2
#===============================================================

uk = input("2. What is the captial of the United Kingdom? ")
uk = uk.upper()
if uk == "LONDON":
    print("That is correct!")
else:
    print("The correct answer is London.")

#===============================================================
#------------------------QUESTION 3
#===============================================================

italy = input("3. What is the captial of Italy? ")
italy = italy.upper()
if italy == "ROME" or "ROMA":
    print("That is correct!")
else:
    print("The correct answer is Rome (or Roma).")

#===============================================================
#------------------------QUESTION 4
#===============================================================

sweden = input("4. What is the captial of Sweden? ")
sweden = sweden.upper()
if sweden == "STOCKHOLM":
    print("That is correct!")
else:
    print("The correct answer is Stockholm.")

#===============================================================
#------------------------QUESTION 5
#===============================================================

germany = input("5. What is the captial of Germany? ")
germany = germany.upper()
if germany == "BERLIN":
    print("That is correct!")
else:
    print("The correct answer is Berlin.")

#===============================================================
#------------------------QUESTION 6
#===============================================================

greece = input("6. What is the captial of Greece? ")
greece = greece.upper()
if greece == "ATHENS" or "ATHINA":
    print("That is correct!")
else:
    print("The correct answer is Athens (or Athina).")

#===============================================================
#------------------------QUESTION 7
#===============================================================

switz = input("7. What is the captial of Switzerland? ")
switz = switz.upper()
if switz == "BERN" or "BERNE" or "BERNA":
    print("That is correct!")
else:
    print("The correct answer is Bern (or Berne or Berna).")

#===============================================================
#------------------------QUESTION 8
#===============================================================

ire = input("8. What is the captial of Ireland? ")
ire = ire.upper()
if ire == "DUBLIN" or "BAILE ATHA CLIATH":
    print("That is correct!")
else:
    print("The correct answer is Dublin.")

#===============================================================
#------------------------QUESTION 9
#===============================================================

spain = input("9. What is the captial of Spain? ")
spain = spain.upper()
if spain == "MADRID":
    print("That is correct!")
else:
    print("The correct answer is Madrid.")

#===============================================================
#------------------------QUESTION 10
#===============================================================

russia = input("10. What is the captial of Russia? ")
russia = russia.upper()
if russia == "MOSCOW" or "MOSKVA":
    print("That is correct!")
else:
    print("The correct answer is Moscow (or Moskva).")