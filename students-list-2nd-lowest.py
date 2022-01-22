n=int(input())
det=[]
mrks=[]
for i in range(n):
    stu=[]
    name=input()
    marks=float(input())
    stu.append(name)
    stu.append(marks)
    mrks.append(marks)
    det.append(stu)
det.sort()
sml=min(mrks)
mrks.sort()
cnt=mrks.count(sml)
for i in range(0,cnt):
    mrks.remove(sml)
sml=min(mrks)
for i in det:
    a=i[1]
    if(a==sml):
        print(i[0])
    
        
