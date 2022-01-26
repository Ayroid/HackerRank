def average(array):
    # your code goes here
    avg=0
    array=set(array)
    l=len(array)
    for i in array:
        avg+=float(i)
    avg=avg/l
    avg="{:.3f}".format(avg)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)