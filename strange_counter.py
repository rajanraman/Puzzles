import sys

n = int(input().strip())

counter = 1
while True:
    if n < (3*counter)-2:
        break
    else:
        counter *= 2

upper_limit = (3*counter)-3
print(upper_limit-n+1)
