#===============================================================
#------------------------VARIABLES
#===============================================================

""" Wow pretty orange comment here woww
    meh meh meh mehhhhhh
    waaaaaaaaaaa
"""

name = "Giennelle Sharlaine C. Akiat"
occu = "Student"
hob = "Digital Art"
father = "Emmanuel R. Akiat"
mother = "Gina Guia Cruzat"
school = "Bath Spa University"
interest = "Lies of P, DMC, Ben 10: Omniverse"
random = "Idk what else to put here"
womp = 10
ok = 90.99

profile = [name, occu, hob, father, mother, school, interest, random, womp, ok]
profile = '\n'.join(str(x) for x in profile)
#profile = '\n'.join(profile)
# ^^^You can just use this if all variables in list are strings

#===============================================================
#------------------------PRINT
#===============================================================

#------------------------INTRODUCTION
print("Welcome to Code Lab - 1", end="\n ============ \n" )

#------------------------PROFILE
print(profile, end="\n ============ \n")

                #PROFILE - Printing Class Types
print(type(profile))
print(type(womp))
print(type(ok))

                #PROFILE - Overwrite "occu"
print(occu)
occu = "Digital Artist"
print(occu, end="\n ============ \n")

#------------------------POEMS...?
print("""According to all laws of aviation
    There is no way a bee should be able to fly
        it's wings are too small to life its fat little body off the ground
            yet the bee flies anyway.""", end="\n ============ \n")

print("""This is a poem,
that I hardly know of.
Nothing feels foreign,
For I can show off""", end="\n ============ \n")

#------------------------SAME LINE REPEATED
for i in range(1,11):
    print(i, end= ".")
    print("This line is repeated 10 times")