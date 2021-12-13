import sys

with open('ex.txt', 'r') as data:
    lines = data.read().splitlines()

class Node(object):
    def __init__(self, name, init_graph):
        self.name = name
        self.init_graph = init_graph
        self.type = self.construct_type()
        self.paths = self.construct_paths()
        self.isVisited = False
    
    def construct_type(self):
        if (any(l.isupper() for l in self.name)):  # big room
            return 'big'
        elif self.name == 'start':
            return 'start'
        elif self.name == 'end':
            return 'end'
        else:  # small room
            return 'small'
    
    def construct_paths(self):
        paths = []
        for line in self.init_graph:
            a, b = line.split('-')
            if a == self.name and b not in paths:
                paths.append(b)
            if b == self.name and a not in paths:
                paths.append(a)
        return paths



class Graph(object):
    def __init__(self, init_graph):
        self.init_graph = init_graph
        self.nodes = self.construct_nodes()
        self.start = self.getStart()
        self.end = self.getEnd()
        self.paths = []

    def construct_nodes(self):
        added = []
        nodes = []
        for line in lines:
            a, b = line.split('-')
            if a not in added:
                added.append(a)
                nodes.append(Node(a, self.init_graph))
            if b not in added:
                added.append(b)
                nodes.append(Node(b, self.init_graph))
        return nodes
    
    def getStart(self):
        for node in self.nodes:
            if node.name == 'start':
                return node
            
    def getEnd(self):
        for node in self.nodes:        
            if node.name == 'end':
                return node
    
    def findAllPaths(self, currNode, currPath=None):
        if currPath == None: #beginning of a path
            print('111111111111')
            currPath =  []
        currPath.append(currNode)
        if currNode.type != 'big':
            print('222222222222')
            currNode.isVisited = True
        print("nodes in currPath: ")
        for node in currPath:
            print(node.name)
        print("end of currPath nodes")
        if currNode == self.end: #we're done with this path
            print('here\'s a path: ')
            for node in currPath:
                print(node.name)
            print('end of path')
            for node in self.nodes:
                node.isVisited = False
            return [currPath]
        paths = []
        for node in self.nodes:
            if node.name in currNode.paths: #child nodes
                print('following node is in ' + str(currNode.name) + '\'s path:')
                print(node.name)
                if not node.isVisited:
                    print('3333333333333333')
                    newpaths = self.findAllPaths(node, currPath)
                    for path in newpaths:
                        paths.append(path)
        return paths

        

ex = Graph(lines)
print(ex.findAllPaths(ex.start))

print(len(ex.findAllPaths(ex.start)))
