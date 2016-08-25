import sys
'''
The algorithm involves the following steps
Start from the right
1. Find the largest x such that P[x]<P[x+1]
2. Find the last largest y from the P[x+1:n] such that P[y] > P[x]
3. swap P[x] and P[y]
4. Reverse P[x+1:n]

'''
def swap(s,i,j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


s = input().strip()
large_char_index = 0
while True:
    pos = -1
    #From the right find i, such that s[i]>s[i-1]
    for i in range(len(s)-1, 0, -1):
        if s[i] > s[i-1]:
            pos = i-1
            break
    #if the pos > -1, then s[x] needs to be replaced else all the characters are in decreasing order which is the largest
    #in the lexicographic order
    if pos > -1:
        #find j from s[i+1:] such that s[y]>s[x]
        for j in range(pos+1, len(s)):
            if s[j] > s[pos]:
                large_char_index = j
        #print(s[pos], s[large_char_index])
        #Swap the smaller and larger value
        s = swap(s, pos, large_char_index)
        #print(s)
        #Reverse the s[pos+1:]
        s = ''.join((s[0:pos+1],s[:pos:-1]))
        print(s)
    else:
        break


