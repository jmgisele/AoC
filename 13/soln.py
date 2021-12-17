#785
import matplotlib.pyplot as plt

with open('data.txt', 'r') as data:
    lines = data.read().splitlines()

#frankenstein of a shorthand but it's just formatting
coords = [[int(a) for a in entry] for entry in [line.split(',') for line in lines if ',' in line]]
dirs = [a.split(' ')[2] for a in lines if ',' not in a and a != '']


def check_duplicates(arr):
    final = []
    for elem in arr:
        if elem not in final:
            final.append(elem)
    return final

# print(checkDuplicates())
def get_map(init_map, directions, first):
    final = init_map.copy()
    for line in directions:
        d, c = line.split('=')
        c = int(c)
        if d == 'x':  # vertical line
            unchanged = [coord for coord in final if (coord[0] < c)]
            new_coords = [[2*c - coord[0], coord[1]] for coord in final if (coord[0] > c)]
            final = check_duplicates(unchanged + new_coords)
        if d == 'y':  # horizontal line
            unchanged = [coord for coord in final if (coord[1] < c)]
            new_coords = [[coord[0],2*c - coord[1]] for coord in final if (coord[1] > c)]
            final = check_duplicates(unchanged + new_coords)
        if (first == True):
            return final

    return final


#pt1
print(len(get_map(coords, dirs, True)))
#pt2

for entry in get_map(coords, dirs, False):
    plt.scatter(entry[0],-entry[1])
plt.show()
