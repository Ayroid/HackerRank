x,y=input().split()
x=int(x)
y=int(y)
j=1

# top part
for i in range((x-1)//2,0,-1):
    print("---"*i,end="")
    print(".|."*j,end="")
    print("---"*i)
    j+=2

# middle line
wel="WELCOME"
print(wel.center(y,"-"))

# bottom part
j-=2
for i in range(1,((x-1)//2)+1):
    print("---"*i,end="")
    print(".|."*j,end="")
    print("---"*i)
    j-=2
