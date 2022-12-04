alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('input.txt', 'r') as data:
    packs = data.read().splitlines()

    # pt 1
    total = 0 

    for pack in packs:
        pack1 = list(pack[:len(pack) // 2])
        pack2 = pack[len(pack) // 2:]

        for char in pack2:
            if char in pack1:
                total += alpha.find(char) + 1
                break

    print(total)

    # pt 2
    total = 0
    i = 0
    repeats = {}

    for pack in packs:
        i += 1
        if i == 1:
            repeats = {key: 1 for key in pack}
            continue
        elif i == 2:
            for char in pack: 
                if char in repeats and repeats[char] == 1:
                    repeats[char] += 1
        else:
            for char in pack:
                if char in repeats and repeats[char] == 2:
                    i = 0
                    repeats = {}
                    total += alpha.find(char) + 1

    print(total)
        


        




        

