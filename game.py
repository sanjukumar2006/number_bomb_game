import random as r

n=int(input("enter the number of element: "))

l=[]
a=0
for _ in range(1,n+1):
    l.append(_)
    a+=1

print(f"the number of element are: {l}")

bomb=r.choice(l)
print(f"bomb: {bomb}")

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
         print("you won")
    
    a-=1
   



