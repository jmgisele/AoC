import re, math

with open('data.txt', 'r') as data:
    linebyline = data.read().splitlines()

incomplete_lines = []
def firstBadChar(line, orig_line=''):
    if orig_line == '':
        orig_line = line
    stripped = line
    #remove all {} until you're left with no valid sets
    stripped = re.sub("\[\]", '', stripped)
    stripped = re.sub("\<\>", '', stripped)
    stripped = re.sub("\{\}", '', stripped)
    stripped = re.sub("\(\)", '', stripped)
    if stripped == line: #you've already removed all valid sets
        for i in range(0, len(stripped)):
            if stripped[i] == '}':
                return 1197
            if stripped[i] == '>':
                return 25137
            if stripped[i] == ')':
                return 3
            if stripped[i] == ']':
                return 57
        incomplete_lines.append(stripped)  #it's invalid
        return 0
    else: #still more to remove baby
        return firstBadChar(stripped, orig_line)

def calcScore(arr):
    total = 0
    for line in arr:
        total += firstBadChar(line)
    return total

print(calcScore(linebyline))


#pt 2
def calcAddTo(line, total=0):
    if len(line) == 0:
        return total
    char = line[-1]
    if char == '{':
        total = (total * 5) + 3
    if char == '<':
        total = (total * 5) + 4
    if char == '(':
        total = (total * 5) + 1
    if char == '[':
        total = (total * 5) + 2
    return calcAddTo(line[:-1], total)

def calcScore(arr):
    total = []
    for line in arr:
        total.append(calcAddTo(line))
    total.sort()
    return total[math.floor(len(total)/2)]

calcScore(incomplete_lines)
