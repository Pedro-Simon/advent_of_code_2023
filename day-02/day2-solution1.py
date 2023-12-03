import re

total_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
game_id_count = 0
file = open("input.txt", "r")

for line in file.readlines():
    cube_amounts = re.findall(r'(\d+) (?=blue|green|red)', line)
    cube_collors = re.findall(r'(blue|green|red)', line)

    game_number = int(re.search(r'(\d.*):', line).group(1))
    is_possible = True

    for i in range(len(cube_amounts)):
        is_possible = is_possible and int(cube_amounts[i]) <= int(total_cubes[cube_collors[i]])
        # print(f'Amounts: {cube_amounts[i]}, Max: {total_cubes[cube_collors[i]]} ==> {is_possible}')
    
    if is_possible:
        game_id_count += game_number

print(game_id_count)
