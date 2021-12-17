with open('data.txt', 'r') as data:
    lines = data.read().splitlines()

#frankenstein of a shorthand but it's just formatting
rules = [line.split(' -> ') for line in lines if ' -> ' in line]
beginning = lines[0]

def recurse_once(inserts, original, new_str=''):
    foundPattern = False
    if len(original) == 1:
        new_str += original
        return new_str
    for chars in inserts:
        if chars[0] == original[0:2]:
            new_str += original[0] + chars[1]
            foundPattern = True
    if foundPattern == False:
        new_str += original[0]
    return recurse_once(inserts, original[1:], new_str)

def recurseMany(n, inserts, original):
    if n == 0:
        return original
    n -= 1
    new = recurse_once(inserts, original)
    return recurseMany(n, inserts, new)


def calcAnswer(final_str):
    dict = {}
    for char in final_str:
        dict[char] = dict[char] + 1 if char in dict.keys() else 1
    maximum = max(dict.values())
    minimum = min(dict.values())
    return maximum - minimum

print(recurseMany(9, rules, beginning))




