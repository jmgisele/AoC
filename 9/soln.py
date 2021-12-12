import numpy as np

with open('data.txt', 'r') as data:
    linebyline = data.read().splitlines()

# pt 1
lowestDict = {}
def checkOneEntry(arr, x, y):
    '''Checks one entry for if its 
    value is lower than the surrounding 
    lowest points. If it is, appends to 
    lowestDict with key as horizontal_vertical
    coord, starting at 0,0 at the top of the 
    array.'''
    val = int(arr[y][x])
    low_X = True
    low_Y = True
    isEndPointX = False
    isEndPointY = False
    if x == 0:
        isEndPointX = True
        if (val >= int(arr[y][x+1])):
            low_X = False
    if (x == len(arr[0]) - 1):
        isEndPointX = True
        if (val >= int(arr[y][x-1])):
            low_X = False
    if not isEndPointX:
        if (val >= int(arr[y][x-1])) or (val >= int(arr[y][x+1])):
            low_X = False
    if y == 0:
        isEndPointY = True
        if (val >= int(arr[y+1][x])):
            low_Y = False
    elif (y == len(arr) - 1):
        isEndPointY = True
        if (val >= int(arr[y-1][x])):
            low_Y = False
    if not isEndPointY:
        if (val >= int(arr[y+1][x])) or (val >= int(arr[y-1][x])):
            low_Y = False
    if low_X and low_Y:
        # it's a match!
        key = '%s_%s' % (str(x), str(y))
        lowestDict[key] = val


def calcSoln(arr):
    for y in range(0, len(arr)):
        for x in range(0, len(arr[0])):
            checkOneEntry(arr, x, y)
    lowest = list(lowestDict.values())
    sum = 0
    for num in lowest:
        risk = 1 + num
        sum += risk
    return sum
print(calcSoln(linebyline))

# pt2
nines_arr = []
for line in linebyline:
    newline = '9' + line + '9'
    nines_arr.append(newline)
nines_arr.insert(0, str('9'*len(nines_arr[0])))
nines_arr.append('9'*len(nines_arr[0]))

def adjacentPoints(point, arr, checked):
    x, y = point
    adj = []
    toCheck = [(x + 1, y), (x - 1, y), (x, y+1), (x, y-1)]
    vals = [arr[y][x + 1], arr[y][x - 1], arr[y+1][x], arr[y-1][x]]
    for i in range(0, len(toCheck)):
        if vals[i] != '9' and toCheck[i] not in checked:
            adj.append(toCheck[i])
    return adj

def basinCheck(low_point, arr, checked=[], endpoints=[]):
    if checked == []:
        checked.append(low_point)
        endpoints.append(low_point)
    needToCheck = False
    for point in endpoints:
        new_points = adjacentPoints(point, arr, checked)
        if len(new_points) != 0:
            needToCheck = True #gotta check these points' children before returning
            endpoints += new_points
            checked += new_points
            endpoints.remove(point)
    if not needToCheck: #all points in checked are endpoints. return set
        return checked
    return basinCheck(low_point, arr, checked, endpoints)

def calcBasinSize(low_pt_dict, arr):
    basins = []
    for location in low_pt_dict.keys():
        x_0, y_0 = location.split("_")
        point = (int(x_0) + 1, int(y_0) + 1) #making up for adding 9s
        basins.append(basinCheck(point, arr, [],[]))
    lengths = []
    for basin in basins:
        lengths.append(len(basin))
    lengths.sort(reverse=True)
    return lengths[0]*lengths[1]*lengths[2]


print(calcBasinSize(lowestDict, nines_arr))
