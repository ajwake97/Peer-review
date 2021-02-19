# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Adrian Wake
# Creation Date: 02/19/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def theGame(): 
  def displayIntro():
    print('You are in a land full of dragons.')
    time.sleep(2)
    print()
    print('In front of you, you see two caves.')
    time.sleep(2)
    print()
    print('In one cave, the dragon is friendly and will share his treasure with you.')
    time.sleep(4)
    print()
    print('In the other, the dragon is greedy and hungry, and will eat you on sight.')
    print()
    time.sleep(2)

  displayIntro()

  def cave():
    cave = input('Which cave will you go into? (1 or 2) ')
    if cave == '1':
      print('You chose cave number 1')
      print()

    else:

      print('You chose cave number 2') 
      print()
  cave()
    
  print('You approach the cave...')
      #sleep for 2 seconds
  time.sleep(2)
  print('It is dark and spooky...')
      #sleep for 2 seconds
  time.sleep(3)
  print('A large dragon jumps out in front of you! He opens his jaws and...')
  print()
    #sleep for 2 seconds
  time.sleep(2)
      
  friendlyCave = (random.randint(0, 1))

  if int(friendlyCave) == 1:
    print('Gives you his treasure!')
  else:
    print('Gobbles you down in one bite!')

theGame()

def playAgain():
  while True:
    again = input('Would you like to play again? \n')
    if again == 'Yes':
      theGame() 
    else: 
      print('Thank you for playing!')
      exit()
playAgain()


