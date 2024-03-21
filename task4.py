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

    def __init__(self, index, value, connections=[], coordinates = None):
        self.value = value
        self.connections = connections
        self.coordinates = coordinates

    def get_neighbours(self):
        #print(np.array(self.connections))
        # list = []
        # list.append()
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

def plot_grid(grid, start, end, path=[]):

    cmap = colors.ListedColormap(['White', 'Black'])
    plt.subplot(3, 1, 1)
    plt.plot(figsize=(10, 10))
    plt.pcolor(grid['small'][::-1], cmap=cmap)
    plt.plot(start['small'][0], start['small'][1], 'ro')
    plt.plot(end['small'][0], end['small'][1], 'go')
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal')
    plt.subplot(3, 1, 2)
    plt.plot(figsize=(20, 20))
    plt.pcolor(grid['medium'][::-1], cmap=cmap)
    plt.plot(start['medium'][0], start['medium'][1], 'ro')
    plt.plot(end['medium'][0], end['medium'][1], 'go')
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal')
    plt.subplot(3, 1, 3)
    plt.plot(figsize=(30, 30))
    plt.pcolor(grid['large'][::-1], cmap=cmap)
    plt.plot(start['large'][0], start['large'][1], 'ro')
    plt.plot(end['large'][0], end['large'][1], 'go')
    plt.gca().invert_yaxis()
    plt.gca().set_aspect('equal')
    plt.tight_layout()
    plt.show()


def bfs(grid, start, end):

    nodes = [1,2,3,4,5,6,7,8,9,10]
    connectivity = grid
    #print(grid)
    graph = Graph(nodes, connectivity)

    #grids['small'][0][0]
    start_node = Node(f'{start}', grid[start[0]][start[1]], connectivity, coordinates=start)
    goal = Node(f'{end}', grid[end[0]][end[1]], connectivity, coordinates=end)


    search_queue = Queue()
    search_queue.push(start_node)
    visited = []

    node_to_check = search_queue.pop(0)
    neighbour = Node()
    node_to_check = goal
    start_node.parent = None

    print(node_to_check.parent)

    # test = Node(index=(3,5),value=0)
    # print(test.get_neighbours)


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


if __name__ == "__main__":
    dict_of_node_examples = {'start': Node(index='potato', value=5, connections='sausage'),
                             'end': Node(index='potato', value=4, connections=[1,2,3]),
                             'key': Node(index='potato', value=1, connections='apple')}
    bfs(grids['small'],starts['small'],goals['small'])
    # print(dict_of_node_examples.items())

    #assert False

    plot_grid(grids, starts, goals)