import sys

def swap(s,i,j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

n = int(input().strip())

for i in range(0, n):
    is_possible = 0
    s = input().strip()
    smaller_index = -1
    #Check if there is x in input s such that s[x] > s[x-1]. s[x] is the element that needs to be replaced with the
    #next larger value. If no x is present then we have hit the largest lexicographic sequence
    for j in range(len(s)-1, 0, -1):
        if s[j] > s[j-1]:
            is_possible += 1
            smaller_index = j-1
            break
    #if we cant find the next lexicographic sequence for input like bb then print no answer
    if smaller_index == -1 and is_possible == 0:
        print("no answer")
    #once we find x, replace with the next larger value from s[x+1:len(s)] and sort the elements in s[x+1:len(s)] in
    #ascending order.
    elif smaller_index > -1:
        for k in range(smaller_index+1, len(s)):
            if s[k] > s[smaller_index]:
                larger_index = k
        s = swap(s, smaller_index, larger_index)
        s = ''.join((s[0:smaller_index+1], s[:smaller_index:-1]))
        print(s)



