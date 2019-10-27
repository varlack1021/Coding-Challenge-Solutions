def validBraces(string):
  stack = []
  right_braces = {'}' : '{', ']': '[', ')':'('}
  
  for index in range(0, len(string)):
    brace = string[index]
    
    if stack == []:
      stack.append(brace)
      continue
    
    if brace in right_braces: 
      
      if stack[-1] == right_braces[brace]:
        stack.pop(-1)
        continue
        
      else:
        return False
    
    stack.append(brace)
 
  return True if not stack else False
  
