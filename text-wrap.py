import textwrap

def wrap(string, max_width):
    words=textwrap.wrap(string,max_width)
    string=""
    for i in words:
        string=string+i+"\n"
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)