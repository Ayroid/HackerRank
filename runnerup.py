# Code to calculate the second largest number in a list

n = int(input("Enter Number of Contestants > "))
arr=[]
print("Enter Scores of All Contestants > ")
for i in range(0,n):
    i=int(input())
    arr.append(i)               #Adding elements to list using append function
#print(arr)

fir=arr[0]
i=0
for i in arr:                   # Calculating the largest element
    if(fir<i):
        fir=i
#print("Largest >",fir)
ctr=arr.count(fir)              # Calculating number of occurances of largest element
#print(ctr)

i=0
j=1
for i in arr:                   # Sort the list
    for j in arr:
        if i<j:
            temp=i
            i=j
            j=temp
#print(arr)

sec=arr[0]
for i in arr[0:len(arr)-ctr]:    #Now we are running a loop from 0 to lenghth-ctr(no of occurnace of largest varible)
    if(sec<i):                   # So that if the largest number occures mutliple times then we can still get 2nd largest
        sec=i
print("Second >",sec)

