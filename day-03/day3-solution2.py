import re

game_id_count = 0
file = open("input.txt", "r")

lines = file.readlines()
total_sum = 0

def has_number(string):
    findings = re.findall(r'[0-9]+', string)
    return len(findings) > 0

def get_values_sum(lines, n_line, start, end):
    adjacent_numbers = []

    # check 1: search for numbers at left
    check_string = lines[n_line][max(start-1, 0)]
    
    list_of_matches=(re.finditer(r'[0-9]+', lines[n_line]))
    for match in list_of_matches:
        match_range = set(range(match.start(), match.end()))
        if bool(set([max(start-1, 0)]).intersection(match_range)):
            adjacent_numbers.append(int(lines[n_line][match.start():match.end()]))
            print(f'At left: {adjacent_numbers}')

    # check 2: search for numbers at right  
    list_of_matches=(re.finditer(r'[0-9]+', lines[n_line]))
    for match in list_of_matches:
        match_range = set(range(match.start(), match.end()))
        if bool(set([min(end, len(lines[n_line]))]).intersection(match_range)):
            adjacent_numbers.append(int(lines[n_line][match.start():match.end()]))
            print(f'At right: {adjacent_numbers}')

    # check 3: search for numbers above
    if n_line-1 >= 0:
        n_above = n_line-1
        min_n = max(start-1, 0)
        max_n = min(end+1, len(lines[n_above]))
        check_range = set(range(min_n, max_n))

        list_of_matches=(re.finditer(r'[0-9]+', lines[n_above]))
        for match in list_of_matches:
            match_range = set(range(match.start(), match.end()))
            if bool(check_range.intersection(match_range)):
                adjacent_numbers.append(int(lines[n_above][match.start():match.end()]))
                print(f'Above: {adjacent_numbers}')

    # check 4: search for numbers bellow
    if n_line+1 <= len(lines)-1:
        n_bellow = n_line+1
        min_n = max(start-1, 0)
        max_n = min(end+1, len(lines[n_bellow]))
        check_range = set(range(min_n, max_n))

        list_of_matches=(re.finditer(r'[0-9]+', lines[n_bellow]))
        for match in list_of_matches:
            match_range = set(range(match.start(), match.end()))
            if bool(check_range.intersection(match_range)):
                adjacent_numbers.append(int(lines[n_bellow][match.start():match.end()]))
                print(f'Bellow: {adjacent_numbers}')
    
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0]*adjacent_numbers[1]
    return 0

for i in range(0,len(lines)):
    list_of_symbols=(re.finditer(r'[\*]', lines[i]))
    for match in list_of_symbols:
        start = int(match.start())
        end = int(match.end())

        line_total = get_values_sum(lines, i, start, end)
        total_sum += line_total
print(total_sum)
