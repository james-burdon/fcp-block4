import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors
class Node:
	'''
	Class to represent a node in an undirected graph
	Each node has a floating point value and some neighbours
	Neighbours is a numpy array representing the row of the adjacency matrix that corresponds to the node
	'''
	def __init__ (self, index, value, connections=[]):
		self.value = value
		self.connections = connections
	def get_neighbours(self):
		return np.where(np.array(self.connections)==1)[0]

class Graph:
	def __init__(self, nodes, adjacency_matrix):
		self.nodes =[]
		
		for (i, node) in enumerate(nodes):
			new_node = Node(i, node, adjacency_matrix[i])
			self.nodes.append(new_node)
		
		self.adjacency_matrix = adjacency_matrix
	
	def plot(self, fig=None, ax=None):
		
		if fig==None:
			fig = plt.figure()
			ax = fig.add_subplot(111)
			ax.set_axis_off()
		
		num_nodes = len(self.nodes)
		network_radius = num_nodes * 10
		ax.set_xlim([-1.1*network_radius, 1.1*network_radius])
		ax.set_ylim([-1.1*network_radius, 1.1*network_radius])
		
		for (i, node) in enumerate(self.nodes):
			node_angle = i * 2 * np.pi / num_nodes
			node_x = network_radius * np.cos(node_angle)
			node_y = network_radius * np.sin(node_angle)
			circle=plt.Circle((node_x,node_y),network_radius/10,fill=False)
			ax.add_patch(circle)
			ax.text(node_x*1.05, node_y*1.05, node.value)
		
			for neighbour_index in range(i+1, num_nodes):
				if node.connections[neighbour_index]:
					neighbour_angle = neighbour_index * 2 * np.pi / num_nodes
					neighbour_x = network_radius * np.cos(neighbour_angle)
					neighbour_y = network_radius * np.sin(neighbour_angle)
					ax.plot((node_x, neighbour_x), (node_y, neighbour_y), color='black')
		plt.show()



class Queue:
	def __init__(self):
		self.queue = []
	def push(self, item):
		self.queue.append(item)
	def pop(self,position):
		if len(self.queue)<1:
			return None
		return self.queue.pop(position)
	
	def is_empty(self):
		return len(self.queue)==0

def bfs():
	grids = {
	'small': np.zeros((10, 10)),
	'medium': np.zeros((20, 20)),
	'large': np.zeros((30, 30))
	}
	# Add obstacles to the grids
	grids['small'][1:4, 2] = 1
	grids['medium'][2:8, 4] = 1
	grids['medium'][10:15, 10:15] = 1
	grids['large'][3:12, 6] = 1
	grids['large'][15:20, 15:20] = 1
	grids['large'][25:28, 5:25] = 1
	starts = {
		'small': [0, 0],
		'medium': [0, 0],
		'large': [0, 0]
	}

	goals = {
		'small': [9, 9],
		'medium': [19, 19],
		'large': [29, 29]
	}
	cmap = colors.ListedColormap(['White','Black'])
	plt.subplot(3,1,1)
	plt.plot(figsize=(10,10))
	plt.pcolor(grids['small'][::-1],cmap=cmap)
	plt.plot(starts['small'][0],starts['small'][1],'ro')
	plt.plot(goals['small'][0],goals['small'][1],'go')  
	plt.gca().invert_yaxis()
	plt.gca().set_aspect('equal')
	plt.subplot(3,1,2)
	plt.plot(figsize=(20,20)) 
	plt.pcolor(grids['medium'][::-1],cmap=cmap)
	plt.plot(starts['medium'][0],starts['medium'][1],'ro')
	plt.plot(goals['medium'][0],goals['medium'][1],'go') 
	plt.gca().invert_yaxis()
	plt.gca().set_aspect('equal')
	plt.subplot(3,1,3)
	plt.plot(figsize=(30,30))
	plt.pcolor(grids['large'][::-1],cmap=cmap)
	plt.plot(starts['large'][0],starts['large'][1],'ro')
	plt.plot(goals['large'][0],goals['large'][1],'go')
	plt.gca().invert_yaxis()
	plt.gca().set_aspect('equal')
	plt.tight_layout()
	plt.show()
	starts = {
		'small': [0, 0],
		'medium': [0, 0],
		'large': [0, 0]
	}

	goals = {
		'small': [9, 9],
		'medium': [19, 19],
		'large': [29, 29]
	}
	# for i in range(len(grids)):
	# 	graph = Graph(nodes, connectivity)
	# 	start_node = graph.nodes[2]
	# 	goal = graph.nodes[-3]
	# 	search_queue = Queue()
	# 	search_queue.push(start_node)
	# 	visited = []

	# 	while not search_queue.is_empty():
	# 		node_to_check = search_queue.pop(0)
			
	# 		if node_to_check == goal:
	# 			node_to_check = goal
	# 			start_node.parent = None
	# 			route = []

	# 			while node_to_check.parent:
	# 				route.append(node_to_check)
	# 				node_to_check = node_to_check.parent
	# 			route.append(node_to_check)
				
			
	# 		for neighbour_index in node_to_check.get_neighbours():
	# 			neighbour = graph.nodes[neighbour_index]
	# 			if neighbour_index not in visited:
	# 				search_queue.push(neighbour)
	# 				visited.append(neighbour_index)
	# 				neighbour.parent = node_to_check

if __name__=="__main__":
	bfs()