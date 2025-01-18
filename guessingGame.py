# Importing rondom built-in library
import random

def numberGuessingGame(): # function is a container
  print("welcome to the Number Guessing Game!")
  randomNumber = random.randint(1, 100) # generates a random number from 1 to 100
  print("I have chosen a number between 1 and 100. Can you guess what it is?")

  # Attempt tracking
  attempts = 0
  guessed = False # is a boolean flag

  # Game Loop
  while not guessed:
    try:
      guess = int(input('Enter your guess: ')) # get user input
      attempts += 1 # increases number of attempts

      if guess < randomNumber:
        print('Too Low! Try again.')
      elif guess > randomNumber:
        print('Too High! Try again.')
      else:
        print(f'Congratulations! You guessed it in {attempts} attempts.')
        guessed = True # stops the loop once correct guess made

    except ValueError: # error handling if input is wrong
      print('Please enter a valid number!')

  print('Thanks for playing!')

numberGuessingGame()