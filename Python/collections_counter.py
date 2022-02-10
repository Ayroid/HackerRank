n=int(input())
sizes=input().split()
nc=int(input())
ern=0
for i in range(0,nc):
    s,p=input().split()
    if s in sizes:
        ern+=int(p)
        sizes.remove(s)
print(ern)