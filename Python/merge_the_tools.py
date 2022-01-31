def merge_the_tools(string, k):
    # your code goes here
    for  i in range(0,len(string),k):
        st=""
        for j in string[i:i+k]:
            if j not in st:
                st+=(j)
        print(st)
            


string, k = input(), int(input())
merge_the_tools(string, k)