a = input()
count={}
odd_values=0

for letter in a:
	if letter in count:
		count[letter]+=1
	else:
		count[letter]=1

for i in list(count.values()):
	if i%2!=0:
		odd_values+=1
	
if odd_values>1:
	print("NO")
else:
	print("YES")