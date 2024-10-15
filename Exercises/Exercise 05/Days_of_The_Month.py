#===============================================================
#------------------------CALENDER
#===============================================================

calender = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

#===============================================================
#------------------------PROCESS
#===============================================================

                    #User Input
month = int(input("Enter the number of a month: "))

                    #If leap Year
if month == 2:
    year = int(input("Enter the year: "))
    if year % 4 == 0:
        print("Number of days: 29")
    else:
        print("Number of days: 28")
else:
    print(f"Number of days: {calender.get(month)}")
