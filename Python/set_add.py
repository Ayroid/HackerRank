n=int(input())
country=set()
for i in range(n):
    cntry=input()
    if cntry not in country:
        country.add(cntry)
print(len(country))