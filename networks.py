import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self, place):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(place)

    def is_empty(self):
        return len(self.queue) == 0


class Node:
    '''
    Class to represent a node in an undirected graph
    Each node has a floating point value and some neighbours
    Neighbours is a numpy array representing the row of the adjacency matrix that corresponds to the node
    '''

    def __init__(self, index, value, connections=[]):
        self.value = value
        self.connections = connections

    def get_neighbours(self):
        return np.where(np.array(self.connections) == 1)[0]


class Graph:
    def __init__(self, nodes, adjacency_matrix):
        self.nodes = []

        for (i, node) in enumerate(nodes):
            new_node = Node(i, node, adjacency_matrix[i])
            self.nodes.append(new_node)

        self.adjacency_matrix = adjacency_matrix

    def plot(self, fig=None, ax=None):
        if fig == None:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.set_axis_off()

        num_nodes = len(self.nodes)
        network_radius = num_nodes * 10
        ax.set_xlim([-1.1 * network_radius, 1.1 * network_radius])
        ax.set_ylim([-1.1 * network_radius, 1.1 * network_radius])

        for (i, node) in enumerate(self.nodes):
            node_angle = i * 2 * np.pi / num_nodes
            node_x = network_radius * np.cos(node_angle)
            node_y = network_radius * np.sin(node_angle)

            # to allow the string values for nodes
            # circle = plt.Circle((node_x, node_y), network_radius / 10, color=cm.hot(node.value), fill=False)
            circle = plt.Circle((node_x, node_y), network_radius / 10, fill=False)
            ax.add_patch(circle)
            ax.text(node_x * 1.05, node_y * 1.05, node.value)

            for neighbour_index in range(i + 1, num_nodes):
                if node.connections[neighbour_index]:
                    neighbour_angle = neighbour_index * 2 * np.pi / num_nodes
                    neighbour_x = network_radius * np.cos(neighbour_angle)
                    neighbour_y = network_radius * np.sin(neighbour_angle)
                    ax.plot((node_x, neighbour_x), (node_y, neighbour_y), color='black')
        plt.show()


nodes = [5, 2, 4, 1]
connectivity = np.array([[0, 0, 1, 1],
                         [0, 0, 1, 1],
                         [1, 1, 0, 0],
                         [1, 1, 0, 0]])
graph = Graph(nodes, connectivity)
graph.plot()


def graph_stuff():
    nodes = ['Cotham', 'Cabot', 'Clifton East', 'Clifton', 'Stoke Bishop', 'Westbury', 'Henleaze', 'Bishopston',
             'Redland']
    # nodes = [1,2,3,4,5,6,7,8,9]
    connectivity = np.array([[0, 1, 1, 0, 0, 0, 0, 0, 1],
                             [1, 0, 1, 1, 0, 0, 0, 0, 0],
                             [1, 1, 0, 1, 1, 0, 0, 0, 0],
                             [0, 1, 1, 0, 1, 0, 0, 0, 0],
                             [0, 0, 1, 1, 0, 1, 1, 0, 1],
                             [0, 0, 0, 0, 1, 0, 1, 0, 1],
                             [0, 0, 0, 0, 1, 1, 0, 1, 1],
                             [0, 0, 0, 0, 0, 0, 1, 0, 1],
                             [1, 0, 0, 0, 1, 1, 1, 1, 0]])
    graph = Graph(nodes, connectivity)
    # graph.legend(['Cotham', 'Cabot', 'Clifton East', 'Clifton', 'Stoke Bishop', 'Westbury', 'Henleaze', 'Bishopston', 'Redland'])
    graph.plot()

    start_node = graph.nodes[0]
    goal = graph.nodes[-1]
    search_queue = Queue()
    search_queue.push(start_node)
    visited = []

    while not search_queue.is_empty():
        node_to_check = search_queue.pop(0)

        if node_to_check == goal:
            node_to_check = goal
            start_node.parent = None
            route = []

            while node_to_check.parent:
                route.append(node_to_check)
                node_to_check = node_to_check.parent
            route.append(node_to_check)

            print([node.value for node in route[::-1]])

        for neighbour_index in node_to_check.get_neighbours():
            neighbour = graph.nodes[neighbour_index]

            if neighbour_index not in visited:
                search_queue.push(neighbour)
                visited.append(neighbour_index)
                neighbour.parent = node_to_check



def bfs():
    # start_node = graph.nodes[0]
    start_node = start
    goal = graph.nodes[-1]
    search_queue = Queue()
    search_queue.push(start_node)
    visited = []
    return


graph_stuff()
