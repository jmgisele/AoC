with open('data.txt', 'r') as data:
    lines = data.read().splitlines()

rules = [line.split(' -> ') for line in lines if ' -> ' in line]
beginning = lines[0]


def setting_up(original):
    dict_pairs = {original[0]: 1, original[len(original) - 1]: 1}
    for i in range(0, len(original) - 1):
        string = original[i:i+2]
        dict_pairs[string] = dict_pairs[string] + 1 if string in dict_pairs.keys() else 1
    return dict_pairs

def one_trial(combos, freq_dict):
    new_dict = {}
    for key, value in freq_dict.items():
        if len(key) == 1:
            new_dict[key] = value
        for entry in combos:
            if key == entry[0]:
                str_1 = key[0] + entry[1]
                str_2 = entry[1] + key[1]
                new_dict[str_1] = value + new_dict[str_1] if str_1 in new_dict.keys() else value
                new_dict[str_2] = value + new_dict[str_2] if str_2 in new_dict.keys() else value
    return new_dict


def run_trials(n, combos, init_dict):
    if n == 0:
        return init_dict
    n -= 1
    new = one_trial(rules, init_dict)
    return run_trials(n, combos, new)

def calc_answer(final_dict):
    dict = {}
    for key, value in final_dict.items():
        if len(key) == 1 and key != beginning[0]:
            dict[key] = dict[key] + 1 if key in dict.keys() else 1
        elif len(key) != 1:
            dict[key[0]] = dict[key[0]] + value if key[0] in dict.keys() else value
    return max(dict.values()) - min(dict.values())

initial_dict = setting_up(beginning)

#pt 1
print(calc_answer(run_trials(10, rules, initial_dict)))

#pt2
print(calc_answer(run_trials(40, rules, initial_dict)))
