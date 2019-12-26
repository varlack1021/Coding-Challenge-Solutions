def convert(self, s: str, numRows: int) -> str:
    #O(N) solution
    #check to see if there is a pattern
    #with strings there is usually a pattern with indexes
    convert = [''] * numRows
    index, step = 0, 1
    
    for x in s:
        convert[index] += x
        
        if index == 0:
            step = 1
            
        elif index == numRows - 1:
            step = -1
        
        index += step
     
    return "".join(convert)