
#Print the platform
def draw(guess):

    if guess ==0:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("-----")

    elif guess==1:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("/|\ ")
        print("-----")

    elif guess ==2:
        print("  ")
        print("  ")
        print("  ")
        print(" |")
        print(" |")
        print(" |")
        print("/|\ ")
        print("-----")

    elif guess ==3:
        print("  ")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/|\ ")
        print("-----")

    elif guess ==4:
        print(" ---")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/|\ ")
        print("-----")

    elif guess ==5:
        print(" ------")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/|\ ")
        print("-----")

    elif guess ==6:
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |")
        print(" |")
        print(" |")
        print("/|\ ")
        print("-----")

    elif guess:
        print(" ------")
        print(" |    |")
        print(" |    O")
        print(" |   -+-")
        print(" |    ()")
        print(" |")
        print("/|\ ")
        print("-----")


# get the secret word from player 1
def get_secret(gamer):
    if gamer =="Y":
        secret = input("\nPLAYER 1: Introduce the secret word, please ").upper()
        while not secret.isalpha() or len(secret)<3 or len(secret)>15:
           secret = input("It seems that the word you gave is invalid, or too hard, or too easy. Try again: ").upper()
        else:
           return secret
    else:
        import random
        #List of Words
        hangmanList = ["dog", "cat", "fish", "dynamic", "banana", "pirate", "ink", "robin", "superman", "wally"]
        random = random.randint(0,9)
        secret = (hangmanList[random]).upper()
        return secret
    

# verify the validity of the input given by player 2
def verify_guess(letter, oldGuess, gamer):
    if gamer == "Y":
        letter = input("\nPLAYER 2: Introduce A letter, please ").upper()
        while not letter.isalpha() or len(letter)!= 1 or letter in oldGuess:
           letter = input("\nOops! Only one letter please, and it needs to be a new one. Try again: ").upper()
        else:
           return letter, oldGuess
    else:
        letter = input("\nIntroduce A letter, please ").upper()
        while not letter.isalpha() or len(letter)!= 1 or letter in oldGuess:
           letter = input("\nOops! Only one letter please, and it needs to be a new one. Try again: ").upper()
        else:
           return letter, oldGuess        

# check if the input of player 2 is contained in the secret word
def check_guess(letter, secret, current):
   change = 0
   temp = list(current)
#   for each match of letter in secret
   for i in range(len(secret)):
      if letter==secret[i]:
         temp[i]=letter
         change = change+1
      else:
         pass
   return temp, change


# check if player 2 has successfully guessed the whole word
def check_win(secret,current):
   if secret==current:
      win = True
   else:
      win = False
   return win



def main():
    guess = 0
    MAX_ATTEMPT = 6
    win = False
    oldGuess = []
    letter = ""
# let the user choose weather he is playing with the computer or with another human being
    gamer = input("\nAre you playing this game with another person?  Y/N ").upper()
    secret = list(get_secret(gamer))
    current = list(secret)
    draw(guess)
    for i in range(len(secret)):
       current[i] = "_"
    print("\nGuess A letter: " ," " .join(map(str, current)), "(" + str(MAX_ATTEMPT) + " guesses left) ")

    while guess < MAX_ATTEMPT and not win:         
        letter, oldGuess = verify_guess(letter, oldGuess, gamer)
        oldGuess = oldGuess + [letter]
        temp, change = check_guess(letter, secret, current)
        if (temp == current):
           guess = guess+1
           draw(guess)
           print("\nYou guessed " + letter + ". No " + letter + " in the rest of the word! ")
#           print("\nYou have previously guessed : " ,"," .join(map(str, oldGuess)))
           print ("\nGuess the word: "," " .join(map(str, current)), "(" + str(MAX_ATTEMPT - guess) + " guesses left) ")
        else:
           current = list(temp)
           print("\nYou guessed " + letter + ". " + str(change) + " " + letter + "s in the word. ")
#           print("\nYou have previously guessed : " ,"," .join(map(str, oldGuess)))
           win = check_win(secret,current)
           if not win:
              print ("\nGuess the word:"," ".join(map(str, current)), "(" + str(MAX_ATTEMPT - guess), "guesses left) ")
           else:
              pass
    else:
        pass
    if win:
        print("\nCONGRATULATIONS! You guessed the word! It was ","" .join(map(str, secret)))      
    else:
        print("\nUh oh Game Over! You've been hanged!")
        guess =7
        draw(guess)
    


def main_game():
    print ("Welcome to Hangman")
    play = input("\nWould you like to play? Y/N ").upper()
    while play == "Y": 
        main()
        play = input("\nPlay again? Y/N ").upper()
    else:
        print("\nOK. Bye!")
        

main_game()

