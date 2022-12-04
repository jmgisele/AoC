with open('input.txt', 'r') as data:
    #pt 1  
    nums = data.read().splitlines()
    tot = 0
    packs = []
    for l in nums:
        if l == '':
            packs.append(tot)
            tot = 0
        else:
            tot += int(l) 

    print(max(packs))

    #pt 2
    second_tot = 0
    for i in range(0,3):
        second_tot += max(packs)
        packs.remove(max(packs))

    print(second_tot)