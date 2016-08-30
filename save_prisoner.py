import sys

test_case = int(input().strip())
for i in range(0,test_case):
    #n, m , s - number of prisoners, number of sweets, starting position
    n, m, s = [int(x) for x in input().split(' ')]
    if m+s > n:
        #if 0 then thats the last position
        if ((s+m) % n)-1 == 0:
            print(n)
        else:
            print(((s+m) % n)-1)
    else:
        print(s+m-1)

