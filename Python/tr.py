arr=[]
i=0
while True:
    i=input("Enter Number > ")
    if(i=="done"):
        break
    else:
        try:
            arr.append(int(i))
        except:
            print("Invalid input")
print(arr)
lar=arr[0]
sml=arr[0]
for i in arr:
    if(lar<i):
        lar=i
    if(sml>i):
        sml=i
print("Maximum is",lar)
print("Minimum is",sml)
