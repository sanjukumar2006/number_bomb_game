import random as r

def choice():
    ask=input("enter your difficulty:\nEasy,Medium,hard:\n--->").lower()
    if ask=="easy":
        print("you have choosen easy level")
        return 3
    elif ask=="medium":
        print("you have choosen medium level")
        return 6
    elif ask=="hard":
        print("you have choosen hard level")
        return 10        

n=choice()

l=[]
a=0
for _ in range(1,n+1):
    l.append(_)
    a+=1

print(f"the number of element are: {l}")

bomb=r.choice(l)
help=input("do you want hint??(y/n)")
if help=="y":
    print(f"bomb: {bomb}")
elif help=="n":
    print("enjoy")    

while a>1:
    
    player=int(input("enter your choice: "))
    

    if player != bomb:
        print("that was not the bomb, you live for now")
        l.remove(player)
        print(l)
        

    else:
        print("you lost, try again later")
        break    
    
    if len(l)==1:
         print("congratulation!")
         print("you won")
    
    a-=1
   



