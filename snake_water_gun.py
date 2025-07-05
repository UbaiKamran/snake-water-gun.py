#Snake Water Gun Game
"""
1 for snake
-1 for water
0 for gun
"""
import random
computer=random.choice([0,1,-1])
print('Enter "s" for snake or "g" for gun or "w" for water')
youstr=input("Enter your choice: ")
youDict={"s":1 , "w":-1 , "g":0}
reverseDict={1:"snake" , -1:"water", 0 :"gun"}
you=youDict[youstr]
#We have created  now 2 variables , one for computer and for player
print(f"You have selected {reverseDict[you]}\nComputer have selected {reverseDict[computer]}")

if(computer==you):
    print("It's a draw")
elif ( (computer == 1 and you == -1) or 
    (computer == -1 and you == 0) or 
    (computer == 0 and you == 1)):
    print("You won!")
else:
    print("You lose")