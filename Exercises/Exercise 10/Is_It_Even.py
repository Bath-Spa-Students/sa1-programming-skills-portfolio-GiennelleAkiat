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