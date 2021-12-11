with open('data.txt', 'r') as data:
    linebyline = data.read().splitlines()
displays_arr = []

vertical_linebyline = ['']*len(linebyline[0])

for i in range(0, len(linebyline)):
    line = linebyline[i]
    for j in range(0, len(line)):
        vertical_linebyline[j] += line[j]

with open('ex.txt', 'r') as data:
    ex_arr = data.read().splitlines()
vertical_ex = ['']*len(ex_arr[0])

for i in range(0, len(ex_arr)):
    line = ex_arr[i]
    for j in range(0, len(line)):
        vertical_ex[j] += line[j]


# pt 1
lowestDict = {}


def checkOneEntry(horiz_arr, x, y):
    '''Checks one entry for if its 
    value is lower than the surrounding 
    lowest points. If it is, appends to 
    lowestDict with key as horizontal_vertical
    starting at 0,0 at the top of the array.
    '''
    val = int(horiz_arr[y][x])
    low_X = True
    low_Y = True
    isEndPointX = False
    isEndPointY = False
    if x == 0:
        isEndPointX = True
        if (val >= int(horiz_arr[y][x+1])):
            low_X = False
    if (x == len(horiz_arr[0]) - 1):
        isEndPointX = True
        if (val >= int(horiz_arr[y][x-1])):
            low_X = False
    if not isEndPointX:
        if (val >= int(horiz_arr[y][x-1])) or (val >= int(horiz_arr[y][x+1])):
            low_X = False
    if y == 0:
        isEndPointY = True
        if (val >= int(horiz_arr[y+1][x])):
            low_Y = False
    elif (y == len(horiz_arr) - 1):
        isEndPointY = True
        if (val >= int(horiz_arr[y-1][x])):
            low_Y = False
    if not isEndPointY:
        if (val >= int(horiz_arr[y+1][x])) or (val >= int(horiz_arr[y-1][x])):
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


# calcSoln(linebyline)
calcSoln(ex_arr)

# pt2
def checkIsBorder(x, y, arr, arrToPushTo):
    '''Checks one point. Returns true
    if point is a border, otherwise
    returns false and adds it to basin array'''
    if x >= len(arr[0]) or x < 0:
        return True
    if y >= len(arr) or y < 0:
        return True
    val = int(arr[y][x])
    if val == 9:
        return True
    #otherwise it's not a border!
    key = '%s_%s' % (str(x), str(y))
    if key not in arrToPushTo:
        arrToPushTo.append(key)
    return False

def basinCheck(x_0, y_0, orig_arr, arr=[]):
    arr_pointers = arr.copy()
    print(arr_pointers)
    if (arr_pointers == []):
        key = '%s_%s' % (str(x_0), str(y_0))
        arr_pointers.append(key)
    for pointer in arr_pointers:
        x , y = pointer.split("_")
        x = int(x)
        y = int(y)
        toggleAllBorders = True
        if not checkIsBorder(x+1, y, orig_arr, arr_pointers):
            toggleAllBorders = False
        if not checkIsBorder(x-1, y, orig_arr, arr_pointers):
            toggleAllBorders = False
        if not checkIsBorder(x, y + 1, orig_arr, arr_pointers):
            toggleAllBorders = False
        if not checkIsBorder(x, y - 1, orig_arr, arr_pointers):
            toggleAllBorders = False
        if toggleAllBorders == True:
            ##they're all borders!
            return len(arr_pointers)
        else: # there's another element somewhere 
            return basinCheck(x + 1, y, orig_arr, arr_pointers) + basinCheck(x - 1, y, orig_arr, arr_pointers) + basinCheck(x, y + 1, orig_arr, arr_pointers) + basinCheck(x, y - 1, orig_arr, arr_pointers)




def calcBasinSize(low_pt_dict, arr):
    print(low_pt_dict)
    for location, low_pt in low_pt_dict.items():
        x_0, y_0 = location.split("_")
        print(x_0, y_0)
        basinSize = basinCheck(x_0, y_0, arr, [])
        print(basinSize)
        break


print(calcBasinSize(lowestDict, ex_arr))


# print(calcBasinSize(lowestDict, linebyline))
