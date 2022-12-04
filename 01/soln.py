with open('input.txt', 'r') as data:
    nums = list(map(lambda num: int(num), data.read().splitlines()))

def calcAvg(arr):
    i = 0
    total = 0
    lastnum = arr[0]
    for num in arr:
        if i != 0 and lastnum < num:
            total += 1
        i+=1
        lastnum = num
    return total

print(calcAvg(nums))

def addThreeArray(arr):
    summed = [sum(z) for z in zip(arr, arr[1:], arr[2:])]
    return summed

print(calcAvg(addThreeArray(nums)))
