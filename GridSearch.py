import sys
# t denotes number of test cases
t = int(input().strip())
match = False

for a0 in range(t):
	#R,C denotes rows and column of the input grid G 
	R,C = input().strip().split(' ')
	R,C = [int(R),int(C)]
	G = []
	G_i = 0
	#Build grid G
	for G_i in range(R):
		G_t = str(input().strip())
		G.append(G_t)
	#r,c denotes the rows and colum of pattern grid P
	r,c = input().strip().split(' ')
	r,c = [int(r), int(c)]
	P = []
	P_i = 0
	#build the pattern P
	for P_i in range(r):
		P_t = str(input().strip())
		P.append(P_t)
	
	for i in range(R):
		for j in range(C):
			#match the first value of the pattern P with the value in grid G
			if G[i][j] == P[0][0]:
	 			match = True
	 			#for each row in pattern see if it matches the row in G
	 			for l in range(r):
	 				# if the row in G does not have matching values in the row in P, break
	 				if P[l] not in G[l+i]:
	 					match = False
	 					break
	 				#this condition is necessary to make sure the pattern matches with the correct index in G
	 				#for example
	 				#G = ['1234', '4321', '9999', '9999']; P = ['12','21']
	 				#Even though the pattern rows 12 and 21 in G[0] and G[1], it is not a match since the index
	 				#is different
	 				elif P[l] != G[l+i][j:j+c]:
	 					match = False
	 					break

	 			if match == True:
	 				break
		if match == True:
			break
	if match == True:
		print("Yes")
	else:
		print("No")
