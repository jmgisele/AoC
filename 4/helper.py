from itertools import chain
from collections import Counter , deque

def find_all_paths(self, currNode, path=None):
    if path == None:
        path = []
    path = path + [currNode]
    if currNode == self.end:
        return [path]
    paths = []
    for node in self.nodes:
        if node.name in currNode.paths:
            if node_allowed(self, path, node):
                newpaths = find_all_paths(self, node, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths  


def node_allowed(graph, path, node):
        small_caves = [k for k, _ in graph.items() if k == k.lower()]
        d = Counter([e for e in path if e in small_caves])
        if (d[node] < 1):
            return True
        else:
            return False

paths = find_all_paths(create_graph(input), 'start', 'end', [])
print(f'part1: {len(paths)}')









