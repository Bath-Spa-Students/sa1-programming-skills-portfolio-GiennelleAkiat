#===============================================================
#------------------------EXERCISE 10
#===============================================================
'''
## Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.
'''

#===============================================================
#------------------------- WORK
#===============================================================

#========= DEF ODD_CHECK
def odd_check(num):
    if num % 2 == 0:
        return f"{num} is even."
    else: 
        return f"{num} is odd."

#========= USING ODD_CHECK() IN MAIN()
def main():
    num = int(input("Enter a number: "))
    print(odd_check(num))

#========= USING MAIN FUNC
if __name__ == "__main__":
    main()