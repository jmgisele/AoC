with open('input.txt', 'r') as data:
    #pt 1  
    rounds = [entry.split(' ') for entry in data.read().splitlines()]

    total = 0
    pts = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
    wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    for (them, me) in rounds:
        if pts[them] == pts[me]:
            total += (pts[me] + 3)
        else:
            total += (pts[me] + 6) if wins[them] == me else (pts[me])
    print(total)

    #pt 2
    total = 0
    losses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    for (them, me) in rounds:
        if me == 'X':
            total += pts[losses[them]]
        if me == 'Y':
            total += (3 + pts[them])
        if me == 'Z':
            total += (6 + pts[wins[them]])
    print(total)


        



