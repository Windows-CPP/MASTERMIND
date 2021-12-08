# This is the funcitons file for MASTERMIND. And yes; I did just CtrlC + CtrlV the code in here- It don't matter all too much. 
# Establishments so that the code ain't angry. Or... Not. I guess I don't need any variables. Cool!
# And yeah, I know there's an issue that won't go away; Whatever, it doesn't produce an error... I think.

from random import randint
from subprocess import call, os

# Variable Establishments, So VS Code Isn't Angry
code = [] # The hidden code array.
difficulty = 0 # 

#** Custom Functions. **#
# These vary per difficulty - Levels 1, 2, and 3. 
# Generates a random 4-digit number, and appends it to code[]. Difficulty Level 1.
def seq():
  for i in range(4):
    code.append(randint(1, 9))

# Generates a random 6-digit number, and appends it to code[]. Difficulty Level 2.
def seq_2():
  for i in range(6):
    code.append(randint(1, 9))

# Generates a random 8-digit number, and appends it to code[]. Difficulty Level 3.
def seq_3():
  for i in range(8):
    code.append(randint(1, 9))



# This code makes me want to die. I HAVE TO REGIGISTR THREE DIFFERENT CHECK FUNCTIONS BECAUSE I CAN'T GET OPTIONAL PARAMETERS TO WORK!!!!! ARGHGHGHGH!
# This should be fixed for the release of v3.0.
def check_1(gs0, gs1, gs2, gs3):
  cou = 0
  # Difficulty Level 1
  if(gs0 == code[0]):
    cou = cou + 1
  if(gs1 == code[1]):
    cou = cou + 1
  if(gs2 == code[2]):
    cou = cou + 1
  if(gs3 == code[3]):
    cou = cou + 1
  
  return cou

def check_2(gs0, gs1, gs2, gs3, gs4, gs5):
  cou = 0
  # Difficulty Level 1
  if(gs0 == code[0]):
    cou = cou + 1
  if(gs1 == code[1]):
    cou = cou + 1
  if(gs2 == code[2]):
    cou = cou + 1
  if(gs3 == code[3]):
    cou = cou + 1
    if(gs4 == code[4]):
      cou = cou + 1
    if(gs5 == code[5]):
      cou = cou + 1
  
  return cou

def check_3(gs0, gs1, gs2, gs3, gs4, gs5, gs6, gs7):
  cou = 0
  # Difficulty Level 1
  if(gs0 == code[0]):
    cou = cou + 1
  if(gs1 == code[1]):
    cou = cou + 1
  if(gs2 == code[2]):
    cou = cou + 1
  if(gs3 == code[3]):
    cou = cou + 1
  
  if(difficulty == 2): # Difficulty Level 2
    if(gs4 == code[4]):
      cou = cou + 1
    if(gs5 == code[5]):
      cou = cou + 1
  
  if(difficulty == 3): # Difficulty Level 3
    if(gs5 == code[6]):
      cou = cou + 1
    if(gs6 == code[6]):
      cou = cou + 1
  
  return cou
  


# (This code was taken from StackOverflow, <https://stackoverflow.com/questions/2084508/clear-terminal-in-python>).
# This code just clears all the text output in the terminal.
def clear():
    # check and make call for specific operating system
    os.system('cls' if os.name == 'nt' else 'clear')


# Well, it's meant to read the leaderboards file, but I'm still working on that. Should be done for v3.0.
def read():
  file1 = open("changelog.txt","r")
  file1.read()
  file1.close()



# The main menu selection screen stuff... I know it's a mess- Not much I can do. Rather in-effiecent; I can fix it later.
def menu():
  start = False # A bool for whether the user selected start on the menu or not. 
  while(start == False):

    clear()
    quit = False
    print("MASTERMIND v2.8.2")
    print("S - Start")
    print("L - Leaderboards")
    #print("LI - License") Not for use yet. Perhaps in the near future?
    print("E - Exit")
    print("")
    str1 = str(input("Enter your choice: "))
    print("")

    # All of this code is just the 'Start' selection...
    if(str1 == "S" or str1 == "s"): # Start
      selected = False # Whether the user has selected a difficulty stting.
      start = True
      difficulty = int(input("Enter a difficulty level (1, 2, or 3.): "))
      while(selected == False):
        if(difficulty == 1): # 'Classic' Difficulty
          seq()
          selected = True
        elif(difficulty == 2): # 'Moderate' Difficulty
          seq_2()
          selected = True
        elif(difficulty == 3): # 'Hard' Difficulty
          seq_3()
          selected = True
        else: # Just an else statement.
          "Invalid input."
      print("")
    
    # The rest of the non-start related selectinos.
    elif(str1 == "L" or str1 == "l"): # Not for use yet. [Leaderboards]
      read()
    #elif(str1 == "LI" or str1 == "li"): Not for use yet. [License]
    elif(str1 == "E" or str1 == "e"): # Exit the program. 
      exit()
    else: # Any other characters
      print("Invalid input.")
      clear()
