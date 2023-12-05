import re

file = open("input.txt", "r")
total_sum = 0

for line in file.readlines():
    line_cleaned = line.strip().split(': ')[1].split(' | ')

    winning_numbers = re.split(r'\s+', line_cleaned[0].strip())
    card_numbers = re.split(r'\s+', line_cleaned[1].strip())
    prizes_winned = set(card_numbers).intersection(set(winning_numbers))

    n_prizes = len(prizes_winned)-1
    if n_prizes > -1:
        total_sum += 2**(n_prizes)
    
print(total_sum)
