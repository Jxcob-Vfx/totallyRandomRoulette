# code for totally random roulette (impossible to win)
# JxcobVFX 2022

# this is the main python file for totally random roulette and the code should run fine in a python3 terminal without other dependencies:
# python3 totallyrandomroulette.py; python3 main.py depending on your filename choice

# the main idea here is roulette, but it's impossible to win because of creative pseudorandom number generation manipulation

# import data libraries
import random
import os
import time
import colorama
from colorama import Fore
# mandatory colorama acknowledgement
colorama

# define main function
def main():
  # main menu
  os.system("clear")
  print("\033[1mTOTALLY RANDOM ROULETTE\033[0m")
  print()
  print("1. Play Roulette")
  print("2. About")
  print()
  menuInput = str(input("> "))
  if menuInput == str("1") or menuInput == str("1."):
    play()
  elif menuInput == str("2") or menuInput == str("2."):
    about()
  else:
    print()
    print("Invalid response.")
    time.sleep(1.5)
    main()

# time based about page subroutine
def about():
  os.system("clear")
  print("\033[1mABOUT TOTALLY RANDOM ROULETTE\033[0m")
  print()
  print("Totally Random Roulette uses a custom Python algorithm.")
  print("This algorithm generates a pseudorandom roulette number.")
  print("The algorithm then excludes any number that would be a win condition for the end user.")
  print()
  time.sleep(6)
  main()

# menu for end user "betting"
def play():
  os.system("clear")
  print("\033[1mPLAY TOTALLY RANDOM ROULETTE\033[0m")
  print()
  print("What do you want to bet on?")
  print()
  print("1. Red or black")
  print("2. Even or odd")
  print("3. Pick a number")
  print("4. Zero")
  print("5. Menu")
  print()
  playInput = str(input("> "))

  # basic end user input analysis
  if playInput == str("1") or playInput == str("1."):
    os.system("clear")
    print("\033[1mRED OR BLACK\033[0m")
    print()
    print("1. Red")
    print("2. Black")
    print()
    redOrBlackInput = str(input("> "))
    if redOrBlackInput == str("1") or redOrBlackInput == str("1."):
      os.system("clear")
      print("\033[1mRED\033[0m")
      print()
      print("Spinning...")
      print()
      time.sleep(3)
      numberRed = random.randint(1,36)
      # the basic idea of this algorithm is that it generates a random integer that is a valid roulette number and just prints it black if the user picks red
      # we are assuming here that the user does not have extensive roulette knowledge and proficiency
      print(Fore.YELLOW + f"\033[1m{numberRed}\033[0m")
      print()
      print(Fore.WHITE + f"Black {numberRed} - You Lose!")
      print()
      time.sleep(2)
      play()
    elif redOrBlackInput == str("2") or redOrBlackInput == str("2."):
      os.system("clear")
      print("\033[1mBLACK\033[0m")
      print()
      print("Spinning...")
      print()
      time.sleep(3)
      numberBlack = random.randint(1,36)
      # same algorithm but for when the end user bets on black
      # note Fore.RED, from the colorama Fore color library
      print(Fore.RED + f"\033[1m{numberBlack}\033[0m")
      print()
      print(Fore.WHITE + f"Red {numberBlack} - You Lose!")
      print()
      time.sleep(2)
      play()
    else:
      os.system("clear")
      print("\033[1mERROR\033[0m")
      print()
      print("Invalid input! Try again...")
      print()
      time.sleep(2)
      play()

  # input analysis and menu for even / odd selection
  elif playInput == str("2") or playInput == str("2."):
    os.system("clear")
    print("\033[1mEVEN OR ODD\033[0m")
    print()
    print("1. Even")
    print("2. Odd")
    print()
    evenOrOdd = str(input("> "))
    if evenOrOdd == str("1") or evenOrOdd == str("1."):
      os.system("clear")
      print("\033[1mEVEN\033[0m")
      print()
      print("Spinning...")
      print()
      # algorithm to check if num % 2 != 0; if there is a remainder
      # if not a new value is generated
      # note booleans in all caps NUMBER_IS_NOT_EVEN = False;
      NUMBER_IS_NOT_EVEN = False
      while NUMBER_IS_NOT_EVEN == False:
        numberEven = random.randint(1,36)
        if numberEven % 2 != 0:
          NUMBER_IS_NOT_EVEN = True
        else:
          pass
      time.sleep(3)
      print(f"\033[1m{numberEven}\033[0m")
      print()
      print(f"{numberEven} is odd - You Lose!")
      print()
      time.sleep(2)
      play()
    elif evenOrOdd == str("2") or evenOrOdd == str("2."):
      os.system("clear")
      print("\033[1mODD\033[0m")
      print()
      print("Spinning...")
      print()
      NUMBER_IS_EVEN = False
      while NUMBER_IS_EVEN == False:
        numberOdd = random.randint(1,36)
        if numberOdd % 2 == 0:
          NUMBER_IS_EVEN = True
        else:
          pass
      time.sleep(3)
      print(f"\033[1m{numberOdd}\033[0m")
      print()
      print(f"{numberOdd} is even - You Lose!")
      print()
      time.sleep(2)
      play()
    else:
      os.system("clear")
      print("\033[1mERROR\033[0m")
      print()
      print("Invalid input! Try again...")
      print()
      time.sleep(2)
      play()
  # prompts end user to input a number as their individual "bet"
  elif playInput == str("3") or playInput == str("3."):
    os.system("clear")
    print("\033[1mPICK A NUMBER\033[0m")
    print()
    numberInput = int(input("What number > "))
    # does not allow end user to input 0 as the number has its own betting option, akin to traditional roulette gameplay
    if numberInput == str("0"):
      os.system("clear")
      print("\033[1mERROR\033[0m")
      print()
      print("You can't pick zero here!")
      print()
      time.sleep(2)
      play()
    else:
      # generates a new number if the generated number is equal to the bet
      os.system("clear")
      NUMBER_FALSE = False
      while NUMBER_FALSE == False:
        number = random.randint(0,36)
        if numberInput == number:
          pass
        else:
          NUMBER_FALSE = True
      print(f"\033[1mYOU BET ON {numberInput}\033[0m")
      print()
      print("Spinning...")
      print()
      time.sleep(3)
      print(f"\033[1m{number}\033[0m")
      print()
      print(f"You picked {numberInput} and the wheel landed on {number}")
      print("You lose!")
      print()
      time.sleep(2)
      play()
      
  elif playInput == str("4") or playInput == str("4."):
    print("\033[1mZERO\033[0m")
    print()
    print("Spinning...")
    print()
    # when end user inputs 0 as "bet"; picks a number between 1 and 36 so as to appear random but allow no margin for a (rare) player win condition.
    # it is most likely true that this would still function as a proof of concept if the code was fully random:
    # numberZero = random.randint(0,36)
    #print(f"{numberZero}")
    # but there is still a slight change (1:36) that random.randint(0,36) will return a value of 0, hence random.randint((0+1),36)
    numberZero = random.randint(1,36)
    time.sleep(3)
    print(f"\033[1m{numberZero}\033[0m")
    print()
    print(f"You bet on 0 and the wheel landed on {numberZero}")
    print("You lose!")
    print()
    time.sleep(2)
    play()

  # menu option in play() subroutine to return end user to main "game menu"
  elif playInput == str("5") or playInput == str("5."):
    os.system("clear")
    print("Returning to main menu...")
    print()
    time.sleep(1.5)
    main()

  # else condition to check for invalid input rather than:
    # if:
      # game
    # else:
      # pass
    # to ensure that the user has another chance to input in the play() subroutine menu
  else:
    os.system("clear")
    print("\033[1mERROR\033[0m")
    print()
    print("Invalid bet input! Try again...")
    print()
    time.sleep(2)
    play()
    

# deploy main function
main()
