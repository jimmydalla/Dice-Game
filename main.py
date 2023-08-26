from colorama import Fore,Back,Style
import random 
import time 
print(Fore.BLUE+"WELCOME TO THE DICE GAME")
print("*************************")
print("\n\n\n")
print(Fore.GREEN+"Hi I'm Jack let's play the dice game")
name = input("May i know your name.............. ")
print("\n\n\n\n")
print(f"Ok {name}, you can start but remember the rule, whoever gets 6 first, they are the winner and the game ends.")
bot = 'Jack'
num = 0
while num!=6:
  num = random.randint(1,6)
  print(Fore.RED)
  print(f"{name} is Rolling the dice and got {num}")
  time.sleep(2)
  if num==6:
    print(f"{name} has won the game")
    break
  time.sleep(2)
  num = random.randint(1,6)
  print(Fore.BLUE)
  print(f"{bot} is Rolling the dice and got {num}")
  if num==6:
    print(f"{bot} has won the game")
