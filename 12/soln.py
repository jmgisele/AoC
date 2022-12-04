with open('data.txt', 'r') as data:
    lines = data.read().splitlines()

class Node(object):
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.type = self.construct_type()
    
    def construct_type(self):
        if (any(l.isupper() for l in self.name)):  # big room
            return 'big'
        elif self.name == 'start':
            return 'start'
        elif self.name == 'end':
            return 'end'
        else:  # small room
            return 'small'



class Graph(object):
    def __init__(self, init_graph):
        self.init_graph = init_graph
        self.nodes = self.construct_nodes()
        self.start = self.get_start()
        self.construct_graph()

    def construct_nodes(self):
        added = []
        nodes = []
        for line in lines:
            a, b = line.split('-')
            if a not in added:
                added.append(a)
                nodes.append(Node(a))
            if b not in added:
                added.append(b)
                nodes.append(Node(b))
        return nodes
    
    def construct_graph(self):
        for node in self.nodes:
            for line in self.init_graph:
                a, b = line.split('-')
                if a == node.name and b not in node.connections:
                    node.connections += [node2 for node2 in self.nodes if node2.name == b]
                if b == node.name and a not in node.connections:
                    node.connections += [node2 for node2 in self.nodes if node2.name == a]


    def get_start(self):
        return [node for node in self.nodes if node.name == 'start'][0]

    #pt1
    def calc_paths1(self, node, visited):
        fin = []
        new_visit = visited + [node]
        if node.name == 'end':
            return [new_visit]
        for n in node.connections:
            if (n.type != 'start') and ((n not in visited) or (n.type == 'big')):
                fin += self.calc_paths1(n, new_visit)
        return fin

    #pt2
    def calc_paths2(self, node, visited):
        fin = []
        new_visit = visited + [node]
        if node.name == 'end':
            return [new_visit]
        for n in node.connections:
            if (n.type == 'big'):
                fin += self.calc_paths2(n, new_visit)
            if (n.type == 'small' or n.type == 'end'):
                small_rooms = [room for room in new_visit if room.type == 'small']
                repeat = any([True for room in small_rooms if small_rooms.count(room) > 1])
                if (repeat and new_visit.count(n) < 1) or (not repeat and new_visit.count(n) < 2):
                    fin += self.calc_paths2(n, new_visit)
        return fin


ex = Graph(lines)
#pt1
print(len(ex.calc_paths1(ex.start, [])))
#pt2
print(len(ex.calc_paths2(ex.start, [])))




