#---------------Problem-----------
'''
The main problem here is that they wanted you to have O(m) space complexity.
For each row and column convert the entire row and column to a zero

#-------------Solution--------------
There are several for loops. It looks a bit ugly haha. I marked each zero with a dash instead of converting right way.
This made sure not to skip a zero or add additional zeroes to the matrix.
Once every zero has been marked. I then converted the entire row and column where the marker was to zero.
I did one conversion of a marker at a time. If when converting to a zero and a marker overlapped, I did not
convert the overlapping marker as to preserve the marker.
Eventually all markers will be removed

I could have used list comprehension but it would have been long and non readable.
'''

def setZeroes(self, matrix: List[List[int]]) -> None:
    row_length = len(matrix)
    column_length = len(matrix[0])
    
    #pass the row and column indexes to be replaced
    def convert_to_zeroes(m, row, column):
        m[row][column] = 0
        
        #convert columns
        for x in range(row_length):
            if m[x][column] != "-":
                m[x][column] = 0 
        
        #convert rows
        for x in range(column_length):
            if m[row][x] != "-":
                m[row][x] = 0
        return m
    
    #Set markers
    for x in range(row_length):
        for y in range(column_length): 
            if matrix[x][y] == 0:
                matrix[x][y] = "-"
    #Find all markers and convert them to zeroes
    for x in range(row_length):
        for y in range(column_length):
            if matrix[x][y] == "-":
                matrix = convert_to_zeroes(matrix, x, y)
    
    return matrix

#----------Optimized Solution------
#This solution implements two of a data structure.

def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0