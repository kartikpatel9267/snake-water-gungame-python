import random
'''1 for snake 
   -1 for water
   0 for gun'''
computer = random.choice([-1,0,1])
playerch = input("enter your choice : ")
youdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}
you = youdict[playerch]
print(f"you choose {reversedict[you]}\n computer choose {reversedict[computer]}")
if(computer==you):
    print("it's   Draw")
else:
    if(computer==-1 and you ==1) :
       print("you win the game ")
    elif(computer==-1 and you==0) :
         print("you loss the game")
    elif(computer== 1 and you== -1) :
         print("you loss the game")
    elif(computer== 1 and you==0) :
         print("you loss the game")
    elif(computer== 0 and you==-1) :
         print("you loss the game")
    elif(computer== 0 and you== -1) :
         print("you loss the game")         
   
    else:
         print("something went wrong")             
