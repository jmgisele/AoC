with open('data.txt', 'r') as data:
    linebyline = data.read().splitlines()
displays_arr = []

for line in linebyline:
    a, b = line.split(" | ")
    displays_arr.append(b.split(" "))

#pt 1

def calcFreq(array_single_line):
    count = 0
    for entry in array_single_line:
        if len(entry) == 2: #count 1s (length 2)
            count += 1
        elif len(entry) == 4: #count4s (length 4)
            count += 1
        elif len(entry) == 3: #count 7s (length 3)
            count += 1
        elif len(entry) == 7: #count 8s (length 7)
            count += 1
    return count

def calcTotalFreq(big_arr):
    count = 0
    for line in big_arr:
        count += calcFreq(line)
    return count

print(calcTotalFreq(displays_arr))

#pt 2
final_arr = []
for line in linebyline:
    a, b = line.split(" | ")
    one_array_line = [a.split(" "), b.split(" ")]
    final_arr.append(one_array_line)

def getCorrelationDict(wires_list):
    correlation_dict = {}
    not_yet_decoded = ['a','b', 'c', 'd', 'e', 'f', 'g'] #these represent PREdecoded letters
    for entry in wires_list:
        if len(entry) == 2: #1 (length 2)
            for i in range(0,2):
                if not entry[i] in correlation_dict:
                    correlation_dict[entry[i]] = ['c', 'f']
        elif len(entry) == 3: #7 (length 3)
            for i in range(0,3):
                if not entry[i] in correlation_dict:
                    correlation_dict[entry[i]] = 'a'
                    not_yet_decoded.remove(entry[i])
        elif len(entry) == 4: #4 (length 4)
            for i in range(0,4):
                if not entry[i] in correlation_dict:
                    correlation_dict[entry[i]] = ['b', 'd']
        elif len(entry) == 7: # 8 (length 7)
            for i in range(0,7):
                if not entry[i] in correlation_dict:
                    correlation_dict[entry[i]] = ['e','g']
    #figure out which two dictionary keys have ['c','f'] as values
    c_f_arr= []
    for key, value in correlation_dict.items():
        if value == ['c', 'f']:
            c_f_arr.append(key)
    # figuring out 0 vs 6 vs 9
    zerosixnine_arr = list(filter(lambda entry: len(entry) == 6, wires_list))
    for entry in zerosixnine_arr:
        #one of them should NOT have one of the keys from above - this is 6!
        #set correlation_dict[whichever they didn't have] = 'c'
        #and set whichever they did have as correlation_dict[whichever they did have] = 'f'
        if not c_f_arr[0] in entry:
            zerosixnine_arr.remove(entry)
            correlation_dict[c_f_arr[0]] = 'c'
            correlation_dict[c_f_arr[1]] = 'f'
            not_yet_decoded.remove(c_f_arr[0])
            not_yet_decoded.remove(c_f_arr[1])
        if not c_f_arr[1] in entry:
            zerosixnine_arr.remove(entry)
            correlation_dict[c_f_arr[0]] = 'f'
            correlation_dict[c_f_arr[1]] = 'c'
            not_yet_decoded.remove(c_f_arr[0])
            not_yet_decoded.remove(c_f_arr[1])
    #check remaining two strings in list - these are 0 or 9
    #find the two letters that they have interchanged
    for letter in zerosixnine_arr[0]:
        if letter not in zerosixnine_arr[1]:
            first = letter
    for letter in zerosixnine_arr[1]:
        if letter not in zerosixnine_arr[0]:
            second = letter
    #check the dict[these_letters] - one should contain d or e
    #whichever letter that is, it's d (or e), and the other is the other
    #so set the one with d to 9 and the one with e to 0
    #and set dict[the letter in 9] = 'd' and dict[the letter in 0] = 'e'
    if 'd' in correlation_dict[first] or  'e' in correlation_dict[second]:
        correlation_dict[first] = 'd'
        correlation_dict[second] = 'e'
        not_yet_decoded.remove(first)
        not_yet_decoded.remove(second)
    elif 'e' in correlation_dict[first] or 'd' in correlation_dict[second]:
        correlation_dict[first] = 'e'
        correlation_dict[second] = 'd'
        not_yet_decoded.remove(first)
        not_yet_decoded.remove(second)
    #figuring out 5 and 2 and 3
    fivetwothree_arr = list(filter(lambda entry: len(entry) == 5, wires_list))
    for letter in 'abcdefg':
        if (letter in not_yet_decoded) and (letter in fivetwothree_arr[0]) and (letter in fivetwothree_arr[1]) and (letter in fivetwothree_arr[2]):
            #whichever letter is in all three 
            #and doesn't correspond to any of the letters we know, that's g, so set dict[that_letter] = 'g'
            correlation_dict[letter] = 'g'
            not_yet_decoded.remove(letter)
            #and the other letter that we haven't figured out to 'b'
            correlation_dict[not_yet_decoded[0]] = 'b'
    #then return the answer :)
    return correlation_dict



def getThisLineDisplay(array_single_line):
    wires, display = array_single_line
    wires.sort(key=len)
    solveDict = getCorrelationDict(wires)
    translatedStrings = []
    for entry in display:
        str = ''
        for char in entry:
            str += solveDict[char]
        translatedStrings.append(str)
    solvednums = ''
    for string in translatedStrings:
        alpha = "".join(sorted(string))
        if alpha == 'abcefg':
            solvednums += '0'
        if alpha == 'cf':
            solvednums += '1'
        if alpha == 'acdeg':
            solvednums += '2'            
        if alpha == 'acdfg':
            solvednums += '3'            
        if alpha == 'bcdf':
            solvednums += '4'            
        if alpha == 'abdfg':
            solvednums += '5'            
        if alpha == 'abdefg':
            solvednums += '6'            
        if alpha == 'acf':
            solvednums += '7'            
        if alpha == 'abcdefg':
            solvednums += '8'            
        if alpha == 'abcdfg':
            solvednums += '9'
    return int(solvednums)            

def calcTotalOutput(big_arr):
    count = 0
    for line in big_arr:
        count += getThisLineDisplay(line)
    return count

print(calcTotalOutput(final_arr))


