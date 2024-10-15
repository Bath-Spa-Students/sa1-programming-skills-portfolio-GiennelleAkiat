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

