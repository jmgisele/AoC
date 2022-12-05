with open('input.txt', 'r') as data:
    pairs = [entry.split(',') for entry in data.read().splitlines()]
    subsets_1 = 0
    subsets_2 = 0
    sets = []

    for pair in pairs:
        one, two = pair
        vals = one.split('-') + two.split('-')
        ints = [int(val) for val in vals]
        sets.append(ints)

    for ints in sets:
        #pt 1
        if (ints[0] <= ints[2] and ints[1] >= ints[3]) or (ints[2] <= ints[0] and ints[3] >= ints[1]):
            subsets_1 += 1
        
        #pt 2
        l_1 = [item for item in range(ints[0], ints[1]+1)]
        l_2 = [item for item in range(ints[2], ints[3]+1)]
        overlap = set(l_1).intersection(l_2)
        if len(overlap) > 0:
            subsets_2 += 1   

    print(subsets_1)
    print(subsets_2)
    

