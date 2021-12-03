with open('data.txt', 'r') as data:
    nums = data.read().splitlines();

# pt 1
print("PART 1")

def calcGr(arr, final=''):
    #if arr is full of empty strings, return final
    if (len(arr[0]) == 0): return final
    sum = 0
    for x in range(0, len(arr)):
        sum += int(arr[x][0])
    newfinal= final + str(int(round(sum / len(arr))))
    return calcGr(list(map(lambda entry: entry[1:], arr)), newfinal)

def calcOpp(a):
    if len(a) == 1:
        return ('1' if a == '0' else '0')
    return calcOpp(str(a[0])) + calcOpp(str(a[1:]))

def calcSoln(a,b):
    return int(a,2) * int(b,2)

gr = calcGr(nums)
er = calcOpp(gr)

print(calcSoln(gr, er))

# pt 2
print("PART 2")

def calcOxGen(arr, i):
    #if arr only has one entry, return arr
    if (len(arr) == 1): return arr[0]
    newarr = []
    ones = zeros = mostCommon = 0
    for x in range(0, len(arr)):
        if (str(arr[x][i]) == '1'): ones += 1  
        else: zeros += 1
    if ones >= zeros: mostCommon = '1' 
    else: mostCommon = '0'
    for y in range(0, len(arr)):
        if str(arr[y][i]) == mostCommon: newarr.append(arr[y])
    m = i + 1
    return calcOxGen(newarr,m)

oxGen = calcOxGen(nums, 0)

def calcScrubRate(arr, i):
    #if arr only has one entry, return arr
    if (len(arr) == 1): return arr[0]
    newarr = []
    ones = zeros = leastCommon = 0
    for x in range(0, len(arr)):
        if (str(arr[x][i]) == '1'): ones += 1  
        else: zeros += 1
    if ones < zeros: leastCommon = '1' 
    else: leastCommon = '0'
    for y in range(0, len(arr)):
        if str(arr[y][i]) == leastCommon: newarr.append(arr[y])
    m = i + 1
    return calcScrubRate(newarr,m)

scrubRate = calcScrubRate(nums, 0)

print(calcSoln(oxGen, scrubRate))

