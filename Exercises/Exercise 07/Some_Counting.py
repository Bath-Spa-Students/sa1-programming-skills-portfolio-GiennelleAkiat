#===============================================================
#------------------------EXERCISE 7
#===============================================================
'''
## Exercise 7: Some Counting - 20 Marks

Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*
'''


#===============================================================
#------------------------0 TO 50
#===============================================================

for i in range(51):
    print(i)

#===============================================================
#------------------------50 to 0
#===============================================================

for i in reversed(range(51)):
    print(i)

#===============================================================
#------------------------30 to 50
#===============================================================

for i in range (30, 51):
    print(i)

#===============================================================
#------------------------50 to 10 in 2
#===============================================================

for i in range(50, 10-2, -2):
    print(i)

#===============================================================
#------------------------100 to 200 in 5
#===============================================================

for i in range (100, 200+5 , 5):
    print (i)