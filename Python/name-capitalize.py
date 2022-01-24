def solve(s):
    j1=" "
    j=""
    string=""
    for i in s:
        j=i
        if j1==" ":
            j=j.upper()
        string+=j
        j1=j
    return string

name=input()
print(solve(name))
