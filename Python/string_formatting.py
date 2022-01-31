def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        dec=i
        oc=oct(i)[2:]
        hexd=hex(i)[2:]
        bi=bin(i)[2:]
        decl=len(str(dec))
        ocl=len(str(oc))
        hexdl=len(str(hexd))
        bil=len(str(bi))
        finl=len(str(bin(number)))-1
        print(" "*(finl-decl-1)+str(dec),end="")
        print(" "*(finl-ocl)+str(oc),end="")
        print(" "*(finl-hexdl)+str(hexd).upper(),end="")
        print(" "*(finl-bil)+str(bi))

n = int(input())
print_formatted(n)