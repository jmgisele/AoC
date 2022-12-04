# pt 1
dict = {"horizontal": 0, "depth": 0}
with open('data.txt', 'r') as data:
    nums = list(map(lambda str: str[0] + str[-1], data.read().splitlines()))

total = {"h": 0, "v": 0}

def calc_pos(arr):
    for item in arr:
        if item[0] == 'd':
            total["v"] += int(item[1])
        elif item[0] == 'u':
            total["v"] -= int(item[1])
        elif item[0] == 'f':
            total["h"] += int(item[1])
    return total["h"]*total["v"]

answer = calc_pos(nums)
#pt 2
new_tot = {"h": 0, "v":0,"aim":0}
def calc_better_pos(arr):
    print(new_tot)
    for item in arr:
        if item[0] == 'd':
            new_tot["aim"] += int(item[1])
        elif item[0] == 'u':
            new_tot["aim"] -= int(item[1])
        elif item[0] == 'f':
            new_tot["h"] += int(item[1])
            new_tot["v"] += new_tot["aim"] * int(item[1])
    return (new_tot, new_tot["h"]*new_tot["v"])

answer2 = calc_better_pos(nums)
