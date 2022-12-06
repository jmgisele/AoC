with open('input.txt', 'r') as data:
    info = data.read().splitlines()
    crate = True
    crates = []
    dirs = []
    num_of_cols = 0

    for line in info:
        if line == '':
            crate = False
            continue
        if ' 1   2   3 ' in line:
            num_of_cols = int(line[-2])
            continue
        crates.append(line) if crate else dirs.append(line)
    
    crate_map = ['placeholder'] + [''] * num_of_cols 
    for line in crates:
        num_zeros = 0
        col = 0
        for char in line:
            if char == ' ':
                num_zeros += 1
            elif char == '[' or char == ']':
                continue
            else:
                col += 1
                if num_zeros > 1:
                    col += num_zeros // 4
                crate_map[col] += (char)
                num_zeros = 0

    crate_map_2 = crate_map.copy()

    # pt 1
    for line in dirs:
        move, coords = line.split(' from ')
        move = int(move.split('move ')[1])
        coords = [int(var) for var in coords.split(' to ')]
        for i in range(0, move):
            crate_map[coords[1]] = crate_map[coords[0]][0] + crate_map[coords[1]]
            crate_map[coords[0]] = crate_map[coords[0]][1:]
    
    top_crates = ''
    for col in range (1, len(crate_map)):
        top_crates += crate_map[col][0]
    print(top_crates)

    # pt 2
    for line in dirs:
        move, coords = line.split(' from ')
        move = int(move.split('move ')[1])
        coords = [int(var) for var in coords.split(' to ')]
        crate_map_2[coords[1]] =  crate_map_2[coords[0]][0:move] + crate_map_2[coords[1]]
        crate_map_2[coords[0]] = crate_map_2[coords[0]][move:]

    top_crates_2 = ''
    for col in range (1, len(crate_map_2)):
        top_crates_2 += crate_map_2[col][0]
    print(top_crates_2)

    