import re

file = open("input.txt", "r")
value_sum = 0

#### PART 2 #####

extended_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def treat_digits(string):
    for i in range(9):
        if extended_numbers[i] in string:
            return str(i+1)
    return string

for line in file.readlines():
    digits_list = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    final_calibration = treat_digits(digits_list[0])+treat_digits(digits_list[-1])

    value_sum += int(final_calibration)

print(value_sum)
file.close()