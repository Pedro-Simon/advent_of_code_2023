import re

game_id_count = 0
file = open("input.txt", "r")

def has_symbol(string):
    findings = re.findall(r'[^a-zA-Z0-9.\s]+', line)
    return len(findings) > 0

for line in file.readlines():
    list_of_matches=(re.finditer(r'[0-9].', line))
    
    for match in list_of_matches:
        start = match.start()
        end = match.end()
        print(f'start: {start}, end: {end}')

    list_of_symbols = has_symbol(line)
    print(list_of_symbols)

# print(game_id_count)
