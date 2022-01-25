if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

avg=0
ctr=0

for k,v in student_marks.items():
    if k==query_name:
        for i in v:
            avg+=float(i)
        avg=avg/3
        avg="{:.2f}".format(avg)
        print(avg)
        ctr+=1
if ctr==0:
    print("Entry Doesn't exist!")

    