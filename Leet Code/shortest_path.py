
from collections import defaultdict
from math import sqrt
from time import time

def map_wires(existingWires):
    rows = existingWires.replace("\n", "-\n").split("\n")
    return dict({((x, y), n) for y, row in enumerate(rows) for x, n in enumerate(row)})

def find_neighbors(coord, valid_nodes):
    x, y = coord
    
    possibilities_straight = {(x+1, y),
                              (x-1, y),
                              (x, y+1),
                              (x, y-1)}

    possibilities_diagonal = {(x+1, y+1),
                              (x-1, y+1),
                              (x-1, y-1),
                              (x+1, y-1)}
    
    return possibilities_straight & valid_nodes, possibilities_diagonal & valid_nodes
    
def build_wiring_diagram(bread_crumb, crystal, goal, start):
    path = bread_crumb[goal]
    
    while path and path != start:
        crystal[path] = 'P'
        path = bread_crumb[path]
    
    return "".join([crystal[key] for key in sorted(crystal.keys(), key=lambda k:(k[1], k[0]))]).replace("-", "\n")

def wire_DHD_SG1(existingWires):
    x = time() + 0.29
    crystal = map_wires(existingWires)
    
    diagonal_distance = sqrt(2)
    
    start = None
    goal = None
    traversable = set()

    for coord, cell in crystal.items():
        if cell == '.':
            traversable.add(coord)
        elif cell == 'S':
            start = coord
        elif cell == 'G':
            goal = coord
            
    valid_nodes = traversable | { goal }

    big_val = float('inf')
    best_distance = defaultdict(lambda:big_val)
    
    best_distance[start] = 0

    bread_crumb = defaultdict(lambda: None)

    item_key_sorter = lambda k: k[1]
    most_promising_distance = 0

    visited = set()
    unvisited_leaves = {start: 0}

    while most_promising_distance < best_distance[goal] and unvisited_leaves != {}:
        if time() > x:
            q = existingWires.replace('\n','Q')

        most_promising_coord, most_promising_distance = min(unvisited_leaves.items(), key=item_key_sorter)

        valid_coords_straight, valid_coords_diagonal = find_neighbors(most_promising_coord, valid_nodes - visited)
        
        visited.add(most_promising_coord)
        _ = unvisited_leaves.pop(most_promising_coord)

        test_plots = {(crd, 1, most_promising_coord) for crd in valid_coords_straight} | {(crd, diagonal_distance, most_promising_coord) for crd in valid_coords_diagonal}

        for child_coord, distance, parent in test_plots:
            parent_best_distance = best_distance[parent]
            best_distance_candidate = parent_best_distance + distance
            
            if best_distance_candidate > best_distance[goal]:
                pass
            elif best_distance_candidate < best_distance[child_coord]:
                bread_crumb[child_coord] = parent
                best_distance[child_coord] = best_distance_candidate
                if child_coord not in visited:
                    unvisited_leaves[child_coord] = best_distance_candidate

    if goal in bread_crumb.keys():
        return build_wiring_diagram(bread_crumb, crystal, goal, start)
    else:
        return "Oh for crying out loud..."

wires = ("S..X ... X.. G..")
string = "consistent"
if string.find("o") == 1:
    print("true")

lis = [1, 2]
lis.append((1, 2)
print(lis)


def myFunc(**kwargs):
  x = None
  y = False

  if not x:
    print("True")
myFunc() 
'''
def addition(n): return n + n

numbers = [1, 2, 3, 4]
result = map(addition, numbers)
colors = ["red", "blue", "orange"]
RGB = ["11" ]
dic = {"r" : "AB12", "b": "22"}
r = 1
g = 2
b = 3
def makeColor(color, value):
    dic[color] = value
    return dic
result = map(makeColor, colors, RGB)

#t = dict(r =r, g=g, b=b)
#print(t)
#print(result)
#print(list(result))
def parse_html_color(color):
    color_value = PRESET_COLORS.get(color.lower(), color)
  
    if len(color_value) == 7:
      r ,g,b=(int(color_value[x:x+2],16) for x in range(1,7,2))
    
    else:
       r,g,b=((int(color_value[x] * 2,16)) for x in range (1,4))
    colors = dict(r=r, g=g, b=b)
    return colors  
similar = {
              "0": ["O", "Q"],
              "Q": ["O", "0"],
              "O": ["Q", "0"],
              "1": ["I", "T"],
              "T": ["I", "1"],
              "I": ["T", "1"],
              "2": ["Z"],
              "5": ["S"],
              "8": ["B"]
  }  
string="trueQ"
string1="a a a "
for key in similar:
    print(key)
    
if "a" not in string1:
    print("trueQ    ")

def similar_license_plates(plate1,plate2):
  print("{}  {}".format(plate1, plate2))
  similar = {
              "0": ["O", "Q"],
              "Q": ["O", "0"],
              "O": ["Q", "0"],
              "1": ["I", "T"],
              "T": ["I", "1"],
              "I": ["T", "1"],
              "2": ["Z"],
              "5": ["S"],
              "8": ["B"],
  }

  for char in plate1:
    if char in plate2:
      return True
    
    if char not in similar:
      continue
    
    else:
      sim_lis = similar[char]
    
      for letter in sim_lis:
        if letter in plate2: 
          return True
          
  return False


print(similar_license_plates("BOX", "XOB"))

x = 0
while x >= 0:
    print(x)
    x = x- 1

  if cut < 0:
    return -1
  slices = None
  if cut ==0:
    slices = 1
    return 1
  prev_number_slices = 1

  x = 1
  while x <= cut:
    
    slices = (x * 2) + (prev_number_slices - x)
    prev_number_slices = slices  
    x = x + 1
  print(slices)
  return slices
    #return cut * 2 + (max_pizza(cut-1) - cut)
'''





import datetime
#how does this format work?
def make_readable(seconds):
  hours, seconds = divmod(seconds, 3600)
  minutes, seconds = divmod(seconds, 60)
  return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]
    #your code here


def decompose(n):
    goal = 0
    result = [n]
    while result:
        current = result.pop()
        goal += current ** 2
        for i in range(current - 1, 0, -1):
            if goal - (i ** 2) >= 0:
                goal -= i ** 2
                result.append(i)
                if goal == 0:
                    result.sort()
                    return result
    return None

def last_digit(n1, n2):
  return pow( n1, n2, 10 )

    #last digit there is also a pattern involved here
    #where the last 4 digits will also repeat

x = 94
x = str(x)
x = list(x)
print(sorted(x))

def stock_list(listOfArt, listOfCat):
    dic = {}
    print(listOfArt)
    result = ""
    
    if listOfArt == [] or listOfCat == []:
        return result
    
    for data in listOfArt:
        book_data = data.split(" ")
        book_code = book_data[0][0]
        quantity = int(book_data[1])
        
        if book_code in dic:  dic[book_code] = dic[book_code] + quantity
        
        else: dic[book_code] = quantity
    
    #can use a .join in instead and list comprehension
    for category in listOfCat:
        if category == listOfCat[len(listOfCat)-1]:
          if category not in dic:
            result += '({} : {})'.format(category, 0)    
          else:
            result += '({} : {})'.format(category, dic[category])  
          break
        if category not in dic:
            result += '({} : {}) - '.format(category, 0)    
        else:
            result += '({} : {}) - '.format(category, dic[category])
    return result
    
def stock_list(stocklist, categories):
  if not stocklist or not categories:
      return ""
  return " - ".join(
      "({} : {})".format(
          category,
          sum(int(item.split()[1]) for item in stocklist if item[0] == category))
      for category in categories)
