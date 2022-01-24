st=input("Enter a String > ")
sub=input("Enter a Substring > ")
i=0
j=len(sub)
ctr=0
while True:
    if st[i:j]==sub:
        ctr+=1
    i+=1
    j+=1
    if(j>len(st)):
        break

print(ctr)
