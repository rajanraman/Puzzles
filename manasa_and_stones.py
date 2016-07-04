N = input()
N=int(N)

for num in range(0,N):
	a=[]
	difference_array=[]
	number_of_stones=int(input())
	difference_array.append(int(input()))
	difference_array.append(int(input()))
	
	result=[]
	'''
	sum will be (n-1-p)*1st difference + p*second difference
	'''
	for p in range(0,number_of_stones):
		result.append((number_of_stones-1-p)*difference_array[0] + p*difference_array[1])
	
	print(" ".join(str(s) for s in sorted(set(result))))
