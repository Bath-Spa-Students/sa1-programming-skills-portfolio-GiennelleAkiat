alien_color = "yellow"

user_input = input("Guess the aliens color: Green, Yellow, or Red? ")
user_input = user_input.lower()

if user_input == alien_color:
    print("You earned 5 points!")
