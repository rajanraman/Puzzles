import sys
#get the length of array (n) and the number of rotations (d)
n, d = input().split(' ')
n = int(n)
d = int(d)
# get the values of array
a = [int(i) for i in input().split(' ')]
rotated_arr = [None] * n
for i in range(0, n):
    position = d % len(a)
    rotated_arr[i] = a[position]
    d += 1

print(' '.join(map(str, rotated_arr)))