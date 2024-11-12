import getpass

#===============================================================
#---------------------HANGMAN PIC-
#===============================================================
hangman_pic = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
  / \\  |
      ==='''
]

#===============================================================
#---------------------FUNCTIONS
#===============================================================

#------------------- DISPLAY THE HANGMAN
def displayboard(wrong_letters, right_letters, word):
    #------- HANGMAN PICS
    print(hangman_pic[len(wrong_letters)]) 
    print()

    #----- No. of blanks
    blanks = "_" * len(word)

    #----- Replace the right letters in blanks
    for i in range(len(word)):
        if word[i] in right_letters:
            #----- Number of blanks
            blanks = blanks[:i] + word[i] + blanks[i+1:]

    # ----- Print the dashes (and letters)
    for letters in blanks:
        print(letters, end = " ")
   
    # ----- Print already guessed letters
    print(f"\n\nAlready Guessed: {", ".join(wrong_letters + right_letters)}\n")

#------------------- GET PLAYER'S GUESS
def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()

        if len(guess) != 1:
            print("Enter a SINGLE letter.")
        elif guess in already_guessed:
            print("Already guessed. Try again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz ":
            print("That is not a letter. Please enter a letter.")
        else:   
            return guess

#------------------- RESTART
def replay():
    print("Do you want to play again? Y / N")
    return input().lower().startswith('y')

#===============================================================
#---------------------VARIABLES
#===============================================================
game_is_done = False

#---- User inputs word to guess
word = getpass.getpass(prompt=str("Enter a word: ")) #--- Uses .getpass to hide the input from players 
word = word.lower()


wrong_letters = ""
right_letters = ""

#===============================================================
#---------------------HANGMAN GAME
#===============================================================

#------------------- WHILE GAME IS NOT DONE
while game_is_done is not True:
    displayboard(wrong_letters, right_letters, word)
    guess = get_guess(wrong_letters + right_letters)

    #---- Right guesses
    if guess in word:
        right_letters += guess
        
        #---- Check is player guessed the word
        found_all_letters = True
        for i in range(len(word)):
            if word[i] not in right_letters:
                found_all_letters = False
        
        #---- Guessed all letters!
        if found_all_letters == True:    
            displayboard(wrong_letters, right_letters, word)
            print(f"""You guessed it. The word was '{word.capitalize()}'!
            
            Right Guesses: {", ".join(right_letters)}
            Wrong Guesses: {", ".join(wrong_letters)}
            Total Guesses: {len(wrong_letters + right_letters)}
            """)
            game_is_done = True

    #---- Wrong guesses
    else:
        wrong_letters += guess

        #---- Hangman got hunged!
        if len(wrong_letters) == len(hangman_pic) - 1:
            displayboard(wrong_letters, right_letters, word)
            print(f"""You lost. The word was '{word.capitalize()}'.
            
            Right Guesses: {", ".join(right_letters)}
            Wrong Guesses: {", ".join(wrong_letters)}
            Total Guesses: {len(wrong_letters + right_letters)}
            """)
            game_is_done = True

    #---- Restart game
    if game_is_done:
        if replay():
            wrong_letters = ""
            right_letters = ""
            game_is_done = False

            word = getpass.getpass(prompt=str("Enter a word: ")) #--- Uses .getpass to hide the input from players 
            word = word.lower()
        else:
            break