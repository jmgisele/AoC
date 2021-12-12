import numpy as np

with open('data.txt', 'r') as data:
    linebyline = data.read().splitlines()

line_arr = []
max_x = 0
max_y = 0
for line in linebyline:
    start, end = line.split(" -> ")
    x_0, y_0 = start.split(',')
    x_1, y_1 = end.split(',')
    newline = [(int(x_0),int(y_0)),(int(x_1),int(y_1))]
    line_arr.append(newline)
    max_x = max(max_x, int(x_0), int(x_1))
    max_y = max(max_y, int(y_0), int(y_1))

#pt 1
map_1 = np.zeros((max_y + 1, max_x + 1), np.int8)
def markLine(line):
    x_a, y_a = line[0]
    x_b, y_b = line[1]
    if x_a == x_b: #vert
        for j in range(min(y_a,y_b),max(y_a,y_b) + 1):
            map_1[j,x_a] += 1
    elif y_a == y_b: #horiz
        for j in range(min(x_a,x_b),max(x_a,x_b) + 1):
            map_1[y_a,j] += 1

def markMap(coords):
    for i in range(0,len(coords)):
        markLine(coords[i])
    return np.count_nonzero(map_1 > 1)

print(markMap(line_arr))


#pt2
map_2 = np.zeros((max_y + 1, max_x + 1), np.int8)
def markAllLine(line):
    x_a, y_a = line[0]
    x_b, y_b = line[1]
    if x_a == x_b: #vert
        for j in range(min(y_a,y_b),max(y_a,y_b) + 1):
            map_2[j,x_a] += 1
    elif y_a == y_b: #horiz
        for j in range(min(x_a,x_b),max(x_a,x_b) + 1):
            map_2[y_a,j] += 1
    else: #45deg
        v = 1 if y_b > y_a else -1
        h = 1 if x_b > x_a else -1
        j = y_a
        for i in range(x_a, x_b + h, h):
            map_2[j,i] += 1
            j += v

def markAllMap(coords):
    for i in range(0,len(coords)):
        markAllLine(coords[i])
    return np.count_nonzero(map_2 > 1)

print(markAllMap(line_arr))

