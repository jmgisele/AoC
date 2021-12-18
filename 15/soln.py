import numpy as np 

with open('data.txt', 'r') as data:
    lines = data.read().splitlines()

class Node(object):
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.cost = int(cost)
        self.connections = []
        self.isVisited = False


class Graph(object):
    def __init__(self, init_graph):
        self.init_graph = init_graph
        self.nodes = self.construct_nodes()
        self.start = self.get_start()
        self.end = self.get_end()
        self.start_costs = self.start_costs()
        self.construct_init_graph()

    def construct_nodes(self):
        nodes = []
        for i in range(0, len(self.init_graph)):
            for j in range (0, len(self.init_graph[0])):
                nodes.append(Node(j,i,self.init_graph[i][j]))
        return nodes


    def get_start(self):
        return [node for node in self.nodes if node.coords == (0,0)][0]

    def get_end(self):
        return [node for node in self.nodes if node.coords == (len(self.init_graph[0]) - 1, len(self.init_graph) - 1)][0]

    def start_costs(self):
        return np.full((len(self.init_graph), len(self.init_graph[0])), float('inf'))

    def construct_init_graph(self):
        for node in self.nodes:
            connections = []
            if node.x == 0 and node.y == 0:
                connections += [node2 for node2 in self.nodes if node2.coords == (0,1) or node2.coords == (1,0)]
            elif node.x == 0:
                connections += [node2 for node2 in self.nodes if node2.coords == (node.x + 1,node.y) or node2.coords == (node.x,node.y - 1) or node2.coords == (node.x,node.y + 1)]
            elif node.y == 0:
                connections += [node2 for node2 in self.nodes if node2.coords == (node.x - 1,node.y) or node2.coords == (node.x + 1,node.y) or node2.coords == (node.x,node.y + 1)]
            elif node.x == len(self.init_graph[0]) - 1 and node.y == len(self.init_graph) - 1:
                continue
            elif node.x == len(self.init_graph[0]) - 1:
                connections += [node2 for node2 in self.nodes if node2.coords == (node.x,node.y - 1) or node2.coords == (node.x,node.y + 1) or node2.coords == (node.x - 1,node.y)]
            elif node.y == len(self.init_graph) - 1:
                connections += [node2 for node2 in self.nodes if node2.coords == (node.x - 1,node.y) or node2.coords == (node.x + 1,node.y) or node2.coords == (node.x,node.y - 1)]
            else:
                connections += [node2 for node2 in self.nodes if node2.coords == (node.x - 1,node.y) or node2.coords == (node.x + 1,node.y) or node2.coords == (node.x,node.y - 1) or node2.coords == (node.x,node.y + 1)]
            node.connections = connections

    #pt2
    def dijkstra_pq(self):
        priority_queue = [[0, self.start]]

        distance_table = self.start_costs
        distance_table[0][0] = 0

        while len(priority_queue) > 0:
            n = priority_queue.pop(0)
            curr_node = n[1]
            curr_dis = n[0]
            neighbors = curr_node.connections
            for neighbor in neighbors:
                distance = curr_dis + neighbor.cost
                neighbor_dist = distance_table[neighbor.y][neighbor.x]
                if neighbor_dist > distance:
                    priority_queue.append([distance, neighbor])
                    priority_queue.sort(key=lambda x: int(x[0])) #keeping it as a pq
                    distance_table[neighbor.y][neighbor.x] = distance
        return distance_table[len(self.init_graph) - 1][len(self.init_graph[0]) - 1]


#pt1
graph_one = Graph(lines)
print(graph_one.dijkstra_pq())

def generate_full_map(lines):
    map_ints = [[int(a) for a in line] for line in lines]
    original_width = len(map_ints[0])
    original_height = len(map_ints)

    for row in range(5):
        for row_new in range(original_height):
            for col in range(5): 
                if row == 0 and col == 0: 
                    continue 
                for col_new in range(original_width):
                    original_value = int(map_ints[row_new][col_new])
                    new_value = original_value + (col + row)
                    while new_value > 9: 
                        new_value -= 9                    
                    map_ints[row_new + row * original_height].append(new_value) 

        if row != 4:
            for row in range(original_height):
                map_ints.append([])
    return [''.join(line) for line in [[str(a) for a in line] for line in map_ints]]

#pt2
graph_two = Graph(generate_full_map(lines))
print(graph_two.dijkstra_pq())

