import random

art='''

  _______  __    __   _______     _______.     _______.   .___________. __    __   _______    .__   __.  __    __  .___  ___. .______    _______ .______      
 /  _____||  |  |  | |   ____|   /       |    /       |   |           ||  |  |  | |   ____|   |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \     
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`   `---|  |----`|  |__|  | |  |__      |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |    
|  | |_ | |  |  |  | |   __|     \   \        \   \           |  |     |   __   | |   __|     |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /     
|  |__| | |  `--'  | |  |____.----)   |   .----)   |          |  |     |  |  |  | |  |____    |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.
 \______|  \______/  |_______|_______/    |_______/           |__|     |__|  |__| |_______|   |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|
                                                                                                                                                              
'''
print(art)

def lod(a):
    for i in range(0,a):
        guess=int(input("make a guess: "))
        if guess==comp_guess:
          print("you made the right guess ")
          print("CONGRATULATIONS!!!!")
          break
        elif guess>comp_guess:
          print("Too high")
          print(f"You have {a-i-1} attempts remaining to guess the number.")
        elif guess<comp_guess:
          print("Too low")
          print(f"You have {a-i-1} attempts remaining to guess the number.")
    
    
        


comp_guess=random.randint(1,100)
print("Welcome to the Number Guessing Game!I'm thinking of a number between 1 and 100")
mode=input("choose your mode of difficulty : easy (or) hard :")
if mode=="easy":
  print(comp_guess)
  lod(10)
else:
  print(comp_guess)
  lod(5)


