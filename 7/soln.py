with open('data.txt', 'r') as data:
    initial_positions = list(map(lambda n: int(n), data.read().split(",")))

base_dict = {}
for crab in initial_positions:
    base_dict[crab] = 0 

for crab in initial_positions:
    base_dict[crab] += 1

maxCrabPos = max(initial_positions)
print(maxCrabPos)

# pt 1

def calc_best_pos(maxCrabPos, crab_dict):
    best_fuel = float('inf')
    best_pos = ''
    for pos in range(0, maxCrabPos + 1):
        #take the last position in crab_list, remove it. this is the position they're all trying to get to
        #calc the ammt of fuel taken for each crab_dict key
        fuel = 0
        for key, value in crab_dict.items():
            if abs((pos - key)) != 0: #if it actually costs fuel
                fuelTaken = value * abs((pos - key))
                fuel += fuelTaken
        if fuel < best_fuel:
            best_fuel = fuel
            best_pos = pos
        pos += 1
    return (best_pos, best_fuel)


print(calc_best_pos(maxCrabPos, base_dict))


#pt 2
##ABSOLUTELY COULD HAVE DONE THIS QUICKER by not re-calcing the
#fuels each time, saving to a dict and accessing....
#but I decided my time was more valuably spent not refactoring.
def calc_fuel(num):
    if num == 1:
        return num
    return num + calc_fuel(num - 1)

def calc_best_pos(maxCrabPos, crab_dict):
    best_fuel = float('inf')
    best_pos = ''
    for pos in range(0, maxCrabPos + 1):
        print(pos)
        #take the last position in crab_list, remove it. this is the position they're all trying to get to
        #calc the ammt of fuel taken for each crab_dict key
        fuel = 0
        for key, value in crab_dict.items():
            if abs((pos - key)) != 0: #if it actually costs fuel
                fuelTaken = value * calc_fuel(abs((pos - key)))
                fuel += fuelTaken
        if fuel < best_fuel:
            best_fuel = fuel
            best_pos = pos
        pos += 1
    return (best_pos, best_fuel)

print(calc_best_pos(maxCrabPos, base_dict))

