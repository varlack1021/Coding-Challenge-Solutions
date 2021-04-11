'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to O

Solution: store the location of zeroes in a dic
'''

def zero_matrix(matrix):
	r = set()
	c = set()
	l = len(matrix)

	for i in range(l):
		for j in range(l):
			if matrix[i][j] == 0:
				r.add(i)
				c.add(j)

	for i in r:
		matrix[i] = [0 for x in range(l)]

	for i in c:
		for j in range(len(matrix)):
			matrix[j][i] = 0

	return matrix

m =  [
		[5, 6, 1, 2],
		[5, 0, 3, 0],
		[0, 2, 2, 2],
		[2, 4, 2, 2]
	]

print(zero_matrix(m))