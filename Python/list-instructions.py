n=int(input())
ins=[]
arr=[]
for i in range(n):
    cmd=input()
    ins.append(cmd)

for i in ins:
    abc=i.split()
    if(abc[0]=="insert"):
        arr.insert(int(abc[1]),int(abc[2]))
    elif(abc[0]=="print"):
        print(arr)
    elif(abc[0]=="remove"):
        arr.remove(int(abc[1]))
    elif(abc[0]=="append"):
        arr.append(int(abc[1]))
    elif(abc[0]=="sort"):
        arr.sort()
    elif(abc[0]=="pop"):
        arr.pop()
    elif(abc[0]=="reverse"):
        arr.reverse()
    else:
        print("Wrong Command!")
