with open('data.txt', 'r') as data:
    initial_fish = list(map(lambda n: int(n), data.read().split(",")))

base_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for fish in initial_fish:
    base_dict[fish] += 1

# day 1 
def countToDay(initial_fish, dayToCalc):
    day = 0
    fish_dict = base_dict.copy()
    for day in range(0, dayToCalc + 1, ):
        total_num_fish = sum(fish_dict.values())
        print(day, fish_dict, total_num_fish)
        new_fishes = fish_dict[0]
        for i in range(0,8):
            fish_dict[i] = fish_dict[i+1]
        fish_dict[6]  += new_fishes
        fish_dict[8] = new_fishes
    return total_num_fish

#pt1
countToDay(base_dict, 80)

#pt 2
countToDay(base_dict, 256)
