from pprint import pprint
from collections import defaultdict


class DFS:

	def __init__(self, edges):
		self.graph = self.create_graph(edges)
		self.visited = []
		self.unvisited = list(self.graph.keys())
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

	def create_graph(self, edges):
		graph = defaultdict(list)
		for edge in edges:
			i = edge[0]
			j = edge[1]

			graph[i].append(j)
			graph[j].append(i)

		return graph

edges = [(1,3), (1,7), (1,2), (2,3), (5,6), (6,8)]
dfs = DFS(edges)
print(dfs.count_disjoint_graphs(), dfs.visited, dfs.sub_graphs)

