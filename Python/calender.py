import calendar

m,d,y=(input().split(" "))

m=int(m)
d=int(d)
y=int(y)

day=int(calendar.weekday(y,m,d))
arr=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(arr[day])