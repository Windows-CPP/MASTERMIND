# MASTERMIND v2.8.2
# See `README.TXT` for more information.

# Imports + Establishments.
from random import randint
from subprocess import call, os
from ext_func import seq, seq_2, seq_3, check_1, check_2, check_3, clear, menu
code = [] # The secret code.
tri = 0 # The number of times the user has tried to break the code.
count = 0 # I... I actually don't know what this variable does... Should probably figure that out.
won = False # Whether the user has won the game or not.
games = 1 # The number of games played.
difficulty = 1 # The selected difficulty (See README.TXT for more information.)


#** Custom Functions. **#
# After four attempts, it works. It just prints the last code that was entered, along with the game's title and number of games played. How did this take me four tries? 
# Note: Update this for higher difficulties BEFORE v3.0, if you can get them fecken' workin'. May need a few `if` statements. 
def comp():
  print("MASTERMIND v2.8.2 - Game " + str(games))
  print("Last attempted code: " + str(gus0) + str(gus1) + str(gus2) + str(gus3) + ". Number correct: " + str(count) + ".")


#************** Main Code **************#
# This is just the title screen- Printed once when the game starts, and not again.
print("MASTERMIND v2.8.2")
print("Developed by Robert Castro, Inspired by 'Mastermind' made by Mordecai Meirowitz")
print("Note: The game only accepts one-digit integers between 1-9.")
print("Additional Note: The only funcionting difficulty as-of v2.8.3 is 1. ")
input("Press 'ENTER' to continue... ")
clear()
menu()
print("\n\n")


# The actual game.
clear()
print("MASTERMIND v2.8.2 - Game " + str(games))
print("Last attempted code: N/A. Number correct: N/A.")

while(count != 4 and won == False):
  tri = tri + 1
  
  # The guesses. These ones are for Diff. Levels 1, 2, and 3. 
  if(tri > 1): # This one is for the base: Diff. Level 1. 
    comp()
  gus0 = int(input("Enter what you think the first number is: "))
  gus1 = int(input("Enter what you think the second number is: "))
  gus2 = int(input("Enter what you think the third number is: "))
  gus3 = int(input("Enter what you think the fourth number is: "))
  if(difficulty >= 2): # Diff. Level 2 + 3 ONLY!
    gus4 = int(input("Enter what you think the fifth number is: "))
    gus5 = int(input("Enter what you think the sixth number is: "))
  elif(difficulty == 3): # Diff. Level 3 ONLY!
    gus6 = int(input("Enter what you think the seventh number is: "))
    gus7 = int(input("Enter what you think the eighth number is: "))

  
  # The checks for the guesses. It's a mess- Along with the whole check logic. Perhaps a near-future update will help... I'll work on it. Maybe fix this by v3.0?
  if(difficulty == 1): # Check for Diff. 1.
    count = check_1(gus0, gus1, gus2, gus3)
  elif(difficulty == 2): # Check for Diff. 2.
    count = check_2(gus0, gus1, gus2, gus3, gus4, gus5)
  elif(difficulty == 3): # Check for Diff. 3.
    count = check_3(gus0, gus1, gus2, gus3, gus4, gus5, gus6, gus7)

  print("")
  print("You entered: " + str(gus0) + str(gus1) + str(gus2) + str(gus3) + ".")
  print("You guessed " + str(count) + " correctly.")
  print("Current attempt:" + str(tri))
  input("Press ENTER to continue...")
  clear()
  print("")

  # Winning + Replay Logic.
  if(count == 4):
    print("You guessed the code correctly. Excellent work. It took you " + str(tri) + " total attempt(s). You have played " + str(games) + " round(s). ")
    play = str(input("Would you like to play again? (Y/N): "))
    games = games + 1

    if(play == "Y" or play == "y"):
      tri = 0
      count = 0
      code = []
      if(games <= 3): 
        seq()
      elif(games > 3): # Increase the difficulty after three games are won.
        seq_2()
      elif(games > 6): # Increase the difficulty after six games are won.
        seq_3()
      print("\n\n")
    elif(play == "N" or play == "n"):
      clear()
      menu()
    else:
      print("Invalid answer.")