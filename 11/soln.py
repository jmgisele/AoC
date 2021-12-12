with open('data.txt', 'r') as data:
    mapOcto = data.read().splitlines()


class Octopus(object):
    def __init__(self, x, y, octopi_map):
        self.x = x
        self.y = y
        self.coord = (x, y)
        self.initial_octopi = octopi_map
        self.energy = int(self.initial_octopi[y][x])
        self.justFlashed = False
        self.neighbors = self.calcNeighbors()

    def getEnergy(self):
        return self.energy
    
    def setEnergy(self, newEnergy):
        self.energy = newEnergy
        return
    def calcNeighbors(self):
        neighbors = []
        x0 = False
        y0 = False
        x9 = False
        y9 = False
        if self.x == 0:
            neighbors.append((self.x+1, self.y))
            x0 = True
        elif self.x == 9:
            neighbors.append((self.x-1, self.y))
            x9 = True
        else:  # not an end- x
            neighbors.append((self.x-1, self.y))
            neighbors.append((self.x+1, self.y))
        if self.y == 0:
            neighbors.append((self.x, self.y + 1))
            y0 = True
        elif self.y == 9:
            neighbors.append((self.x, self.y - 1))
            y9 = True
        else:  # not an end-y
            neighbors.append((self.x, self.y + 1))
            neighbors.append((self.x, self.y - 1))
        if not x0 and not x9 and not y0 and not y9:  # not an end case
            neighbors.append((self.x + 1, self.y + 1))
            neighbors.append((self.x + 1, self.y - 1))
            neighbors.append((self.x - 1, self.y - 1))
            neighbors.append((self.x - 1, self.y + 1))
        if x0 and y0:
            neighbors.append((self.x + 1, self.y + 1))
        elif x0 and y9:
            neighbors.append((self.x + 1, self.y - 1))
        elif x0 and not y0 and not y9:
            neighbors.append((self.x + 1, self.y + 1))
            neighbors.append((self.x + 1, self.y - 1))
        elif x9 and y9:
            neighbors.append((self.x - 1, self.y - 1))
        elif x9 and y0:
            neighbors.append((self.x - 1, self.y + 1))
        elif x9 and not y9 and not y0:
            neighbors.append((self.x - 1, self.y + 1))
            neighbors.append((self.x - 1, self.y - 1))
        elif y0 and not x0 and not x9:
            neighbors.append((self.x + 1, self.y + 1))
            neighbors.append((self.x - 1, self.y + 1))
        elif y9 and not x0 and not x9:
            neighbors.append((self.x + 1, self.y - 1))
            neighbors.append((self.x - 1, self.y - 1))
        return neighbors


class Octopi(object):
    def __init__(self, octopi_map):
        self.octopi_map = octopi_map
        self.octopi = self.generateOctopi()
        self.numFlashes = 0
        self.numTimeSteps = 0
        self.hasSynced = False
        self.firstSync = False

    def generateOctopi(self):
        octopi = {}
        for x in range(0, 10):
            for y in range(0, 10):
                octopi[(x,y)] = Octopus(x, y, self.octopi_map)
        return octopi

    def oneTimeStep(self):
        flashesThisStep = 0
        for oct in self.octopi.values():
            e_0 = oct.getEnergy()
            oct.setEnergy(e_0+1)
        while True: #break when no more flashing
            oneFlashed = False
            for oct in self.octopi.values():
                if not oct.justFlashed: #if it's flashed this round, it's done
                    if oct.getEnergy() > 9: #if its energy is high enough
                        oneFlashed = True #flash!
                        flashesThisStep += 1
                        oct.justFlashed = True
                        for neighbor in oct.neighbors:
                            this_neighbor = self.octopi[neighbor]
                            e_0 = this_neighbor.getEnergy()
                            this_neighbor.setEnergy(e_0 + 1)
            if oneFlashed == False: #done flashing. reset stuff.
                break
        #pt 2
        allFlashed = True
        for oct in self.octopi.values():
            if not oct.justFlashed: 
                allFlashed = False
                break
        if allFlashed and not self.hasSynced:
            self.firstSync = self.numTimeSteps
            self.hasSynced = True

        for oct in self.octopi.values():
            if oct.justFlashed:
                oct.setEnergy(0)
                oct.justFlashed = False
        self.numFlashes += flashesThisStep

    def simulateSteps(self, steps):
        for i in range(0, steps):
            self.numTimeSteps += 1
            self.oneTimeStep()


octo = Octopi(mapOcto)

octo.simulateSteps(100)
print(octo.numFlashes)

octo.simulateSteps(500)
print(octo.firstSync)
