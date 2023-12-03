import re

total_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

cumulated_power = 0
file = open("input.txt", "r")

for line in file.readlines():
    game_number = int(re.search(r'(\d.*):', line).group(1))

    cube_amounts = re.findall(r'(\d+) (?=blue|green|red)', line)
    cube_collors = re.findall(r'(blue|green|red)', line)

    max_set = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for i in range(len(cube_amounts)):
        # print(f'Color: {cube_collors[i]}, Amounts: {cube_amounts[i]}, Max: {max_set[cube_collors[i]]}')
        max_set[cube_collors[i]] = max(int(max_set[cube_collors[i]]), int(cube_amounts[i]))
    
    game_power = max_set['red']*max_set['green']*max_set['blue']
    cumulated_power += game_power
    
print(cumulated_power)
