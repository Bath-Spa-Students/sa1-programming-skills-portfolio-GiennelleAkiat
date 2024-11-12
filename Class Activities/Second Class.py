#===============================================================
#--------------------STRING CONCATENATION
#===============================================================
#-------------------Through Variables
text = "This is " + "ridiculous."
print(text)

#-------------------Through Print
print("Printing" + " a bunch of" + " stuff.")

#-------------------Adding space
name = "Giennelle Sharlaine C. Akiat"
occu = "Student"
hob = "Digital Art"
print(name, occu, hob, sep = " | ")
                    #ALTERNATIVELY
profile = name + " | " + occu + " | " + hob
print(profile)

print(f"You're a {occu}.")

in_name = input("Enter your name: ")
print(in_name)