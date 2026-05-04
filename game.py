import random as r

def choice():
    while True:
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
        else:
            print("please choose from the given option")    

n=choice()

l=[]
for _ in range(1,n+1):
    l.append(_)
    

print(f"The element are: {l}")

bomb=r.choice(l)
while True:
    hint=input("do you want hint??(y/n)").lower()
    if hint in ['y','n']:
        break
    
    else:
        print("please choose from y/n")
        print("y is yes")
        print("n is no")    


if hint=="y":
    print(f"bomb: {bomb}")
elif hint=="n":
    print("enjoy")    

while len(l)>1:
    
    try:
        player=int(input("enter your choice: "))
        if player in l:
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
    
            
        else:
            print("please choose number from the list ")
    except ValueError:
        print("please enter a number ")