st = input("Enter String > ")
sub = input("Enter Substring > ")
ctr=0
for i in range(len(st)-len(sub)+1):
    if st[i:i+len(sub)]==sub:
        ctr+=1
print(ctr)
