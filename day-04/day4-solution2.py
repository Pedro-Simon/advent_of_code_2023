import re

file = open("input.txt", "r")
lines = file.readlines()
list_scratches = [1] * len(lines)

total_sum = 0

for i in range(0, len(lines)):
    line_cleaned = lines[i].strip().split(': ')[1].split(' | ')

    winning_numbers = re.split(r'\s+', line_cleaned[0].strip())
    card_numbers = re.split(r'\s+', line_cleaned[1].strip())
    matching_numbers = set(card_numbers).intersection(set(winning_numbers))

    n_matches = len(matching_numbers)

    for r in range(1, n_matches+1):
        if i+r < len(list_scratches):
            list_scratches[i+r] += list_scratches[i]
            print(f'Added {list_scratches[i]} to card {i+r}')
        else:
            pass

    
print(sum(list_scratches))
