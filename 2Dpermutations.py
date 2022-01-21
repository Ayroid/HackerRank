x=int(input())
y=int(input())
z=int(input())
n=int(input())
per=[]
ans=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
             lst=[i,j,k]
             per.append(lst)

for i in per:
    sum=0
    for j in i:
        sum=sum+int(j)
    if sum!=n:
        ans.append(i)

print(ans)
