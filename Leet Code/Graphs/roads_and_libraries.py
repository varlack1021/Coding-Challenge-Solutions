from pprint import pprint
from collections import defaultdict

class DFS:
    
    def __init__(self, n, edges):
        self.graph = self.create_graph(edges)
        self.visited = []
        self.unvisited = [n+1 for n in range(n)]
        self.sub_graphs = 0
        
    def dfs(self, node):
        self.visited.append(node)
        self.unvisited.remove(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
    
    def count_disjoint_graphs(self):
        while self.unvisited:
            self.dfs(self.unvisited[0])
            self.sub_graphs += 1
        return self.sub_graphs
    
    def create_graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            i = edge[0]
            j = edge[1]
            
            graph[i].append(j)
            graph[j].append(i)
    
        return graph

        
if __name__ == '__main__':
    cities = []
    m = 0
    n = 2
    c_road = 1
    c_lib = 102
    dfs = DFS(n, cities)
    roads = len(dfs.graph.keys()) - 1 if m > 0 else 0
    sub_graphs = dfs.count_disjoint_graphs()

    if c_lib < c_road:
        print( c_lib * n)
    else:
    	print("{} * {} + {} * {} ".format(c_road, roads, sub_graphs, c_lib))
    	print( (c_road * roads + sub_graphs * c_lib))  