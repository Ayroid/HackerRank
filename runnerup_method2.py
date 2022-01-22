from re import A


arr=[]
print("Enter Elements into list & write 'stop' after entering all elements")
while True:
    i=input()
    if(i=="stop"):
        break
    else:
        arr.append(int(i))
print(arr)
sec=0
arr.sort()
print(arr)
l=len(arr)
for i in range(0,l):
    if(arr(l-i+1)!=arr(l-i)):
        sec=min(arr(l-i+1),arr(l-i))
        break
print(sec)
