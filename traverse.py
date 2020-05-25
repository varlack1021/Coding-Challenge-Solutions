def wire_DHD_SG1(existingWires):
    loc, curr, next, prev, prev_prev, old_loc = 0, 0, 0, 0, 0, 0
    solutions = []
    wires = existingWires.split("\n")
    length_path = -1
    
    for i in range(len(wires)):
      
      if "S" in wires[i]:
        loc = wires[i].find("S")
        curr = wires[i]
        
        if i > 0:
          prev_prev = prev
          prev = wires[i-1]
        
        if i < len(wires):
          next = wires[i + 1]
          
    moves = [ {"U": 0,}, {"D": 0}, {"L":-1}, {"R":1},
      {"UR": 1}, {"UL": -1}, {"DL": -1}, {"DR": 1}]
    
    i = 0
    
    while i < len(moves):
      move = moves[i]
      key = None
      value = None
      
      for key in moves[i]:
        key = key
        value = moves[i][key]
        
      if not traverse_path(key, loc, value):
      
        if i > 7 and curr[loc] != 'S':
          curr = prev
          next = curr
          prev = prev_prev
          loc = old_loc
          i = 0
          continue
        
        if i > 7 and curr[loc] == 'S':
          if not solutions:
            return "Oh for crying out loud..."
          else:
            return solutions[0]
        
          #need to replace the 'P' with a dot so it would require another function tbh
      

    # Your code here!
    

  def traverse_path(move_type, loc, move_value ):
      new_loc = loc + moves_value
      
      if new_loc < 0 or new_loc > len(curr):
        return False
      
      if move_type == ("U" or "UL" or "UR"):
        #Checks if new string is valid
        if wires.index(curr) - 1 < 0:
          return False
        curr = prev
        prev_prev = prev
        next = curr
        prev = wires [wires.index(curr) - 1 ]
        
      if moves_type == ("D" or "DL" or "DR"):
        #Checks if new string is valid
        if wires.index(curr) + 1 > len(wires):
          return False

        curr = next
        prev_prev = prev
        prev = curr 
        next = wires[wires.index(cur) + 1]

      old_loc = loc
      loc = new_loc

def traverse_wires():
  graph = {
  "1": "X..S"
  "2": "XX.X"
  "3": "G..X"
  }

  real_graph = {
  "1": [(1, 2), (1, )]
  }
