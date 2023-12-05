import re

game_id_count = 0
file = open("input.txt", "r")

lines = file.readlines()
total_sum = 0

def has_symbol(string):
    findings = re.findall(r'[^a-zA-Z0-9.\s]+', string)
    return len(findings) > 0

def is_valid_number(lines, n_line, start, end):
    # check 1: search for symbols at left
    check_string = lines[n_line][max(start-1, 0)]
    result = has_symbol(check_string)
    if result:
        return result

    # check 2: search for symbols at right
    check_string = lines[n_line][min(end, len(lines[n_line]))]
    result = has_symbol(check_string)
    if result:
        return result

    # check 3: search for symbols above
    if n_line-1 >= 0:
        n_above = n_line-1
        min_n = max(start-1, 0)
        max_n = min(end+1, len(lines[n_above]))

        check_string = lines[n_above][min_n:max_n]
        result = has_symbol(check_string)
        if result:
            return result

    # check 4: search for symbols bellow
    if n_line+1 <= len(lines)-1:
        n_bellow = n_line+1
        min_n = max(start-1, 0)
        max_n = min(end+1, len(lines[n_bellow]))

        check_string = lines[n_bellow][min_n:max_n]
        result = has_symbol(check_string)
        if result:
            return result  
    return False

for i in range(0,len(lines)):
    list_of_matches=(re.finditer(r'[0-9]+', lines[i]))

    for match in list_of_matches:
        start = int(match.start())
        end = int(match.end())
        decision = is_valid_number(lines, i, start, end)

        if decision:
            total_sum += int(lines[i][start:end])
print(total_sum)
