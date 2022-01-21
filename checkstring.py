from hmac import trans_36


str=input()
t1=0
t2=0
t3=0
t4=0
t5=0
for i in str:
    if i.isalnum():
        t1=1
        break

for i in str:
    if i.isalpha():
        t2=1
        break

for i in str:
    if i.isdigit():
        t3=1
        break

for i in str:
    if i.islower():
        t4=1
        break

for i in str:
    if i.isupper():
        t5=1
        break

if t1==1:
    print("True")
else:
    print("False")
if t2==1:
    print("True")
else:
    print("False")
if t3==1:
    print("True")
else:
    print("False")
if t4==1:
    print("True")
else:
    print("False")
if t5==1:
    print("True")
else:
    print("False")  

