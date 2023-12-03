import re

file = open("input.txt", "r")
value_sum = 0

#### PART 1 #####

for line in file.readlines():
    digits_list = re.findall(r'(\d)', line)
    final_calibration = digits_list[0]+digits_list[-1]

    value_sum += int(final_calibration)
    
print(value_sum)
file.close()
