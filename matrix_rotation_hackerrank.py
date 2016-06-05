#Get the number of rows(R), columns(C) and number of rotations(N)
R,C,N = input().split()
R=int(R)
C=int(C)
N=int(N)

#Build the input matrix
matrix=[]
for x in range(R):
	matrix.append(input().split())
	pass
#Add each layer to the list and then add the rotated version to the matrix
linear_list=[]
rotations=0
if C>R:
	rotations=R
else:
	rotations=C
for i in range(0,rotations//2):
	linear_list.clear()
	for j in range(0+i,i+1):
		for k in range(j,C-j):
			linear_list.append(matrix[j][k])
	for j in range(i+1, R-i-1):
		for k in range(C-i-1,C-i):
			linear_list.append(matrix[j][k])
	for j in range(R-i-1,R-i):
		for k in range(C-i-1,i,-1):
			linear_list.append(matrix[j][k])
	for j in range(R-i-1,i,-1 ):
		for k in range(i,i+1):
			linear_list.append(matrix[j][k])
	#print(linear_list)
	position = N%(len(linear_list))
	if position>0:
		#print("The list",position,len(linear_list))
		for j in range(0+i,i+1):
			for k in range(j,C-j):
				#print("The list",position,len(linear_list),j,k)
				matrix[j][k]=linear_list[position]
				position=(position+1)%len(linear_list)
		for j in range(i+1, R-i-1):
			for k in range(C-i-1,C-i):
				#print("The list",position,len(linear_list),j,k)
				matrix[j][k]=linear_list[position]
				position=(position+1)%len(linear_list)
				#print("The list",position,len(linear_list),j,k)
		for j in range(R-i-1,R-i):
			for k in range(C-i-1,i,-1):
				#print("The list",position,len(linear_list),j,k)
				matrix[j][k]=linear_list[position]
				position=(position+1)%len(linear_list)
				#print("The list",position,len(linear_list),j,k)
		for j in range(R-i-1,i,-1 ):
			for k in range(i,i+1):
				#print("The list",position,len(linear_list),j,k)
				matrix[j][k]=linear_list[position]
				position=(position+1)%len(linear_list)
				#print("The list",position,len(linear_list),j,k)
		#print("The matrix ",ma)
#print matrix
for i,row in enumerate(matrix):
	print(' '.join(row))

