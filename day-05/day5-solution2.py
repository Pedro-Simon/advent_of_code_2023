import re
import pandas as pd

file = open("input.txt", "r")
lines = file.readlines()
seeds = re.split(r'\s+', lines[0][7:].strip())

def get_map(ranges):
    # create list of lists. Ex: [source_start, destination_start, map_size]
    map_destination = []
    for i in range(ranges[0], ranges[1]-1):
        if not lines[i].strip() == '':
            new_row = lines[i].strip().split(' ')
            map_destination.append((int(new_row[1]), int(new_row[0]), int(new_row[2])))
    return map_destination

def get_seed_ranges(seeds):
    # create list of lists. Ex: [seed_start, current_start, seed_size]
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_start = int(seeds[i])
        seed_size = int(seeds[i+1])
        seed_ranges.append((seed_start, seed_start, seed_size))
    return seed_ranges

def apply_destination_rules(seed_ranges, destination_ranges):
    # Applies the mapping solution to each range, considering the starting seed
    solutions = []
    for (source_start, destination_start, map_size) in destination_ranges:
        source_end = source_start + map_size
        repeat_list = []

        while seed_ranges:
            (seed_start, current_start, seed_size) = seed_ranges.pop()

            # print(f'mapping = ({source_start}, {destination_start}, {map_size})')
            # print(f'seed_range = ({seed_start}, {current_start}, {seed_size})')

            current_end = current_start + seed_size
            left = (seed_start, current_start, min(current_end, source_start)- current_start)
            inner = (seed_start + (current_start - max(current_start, source_start)) , max(current_start, source_start), min(current_end, source_end)-max(current_start, source_start))
            right = (seed_start + (current_start - max(current_start, source_end)), max(current_start, source_end), current_end - max(current_start, source_end))
            # left
            if left[2] > 0:
                # print(f'LEFT: {left}')
                repeat_list.append(left)
            # inner
            if inner[2] > 0:
                # print(f'INNER: {(inner[0], inner[1]+destination_start-source_start, inner[2])}')
                solutions.append((inner[0], inner[1]+destination_start-source_start, inner[2]))
            # right
            if right[2] > 0:
                # print(f'RIGHT: {right}')
                repeat_list.append(right)
            
        seed_ranges = repeat_list
    return solutions + seed_ranges

for i in range(0, len(lines)):

    if 'humidity-to-location' in lines[i]:
        start_humidity2location = i+1
    elif 'temperature-to-humidity' in lines[i]:
        start_temperature2humidity = i+1
    elif 'light-to-temperature' in lines[i]:
        start_light2temperature = i+1
    elif 'water-to-light' in lines[i]:
        start_water2light = i+1
    elif 'fertilizer-to-water' in lines[i]:
        start_fertilizer2water = i+1
    elif 'soil-to-fertilizer' in lines[i]:
        start_soil2fertilizer = i+1
    elif 'seed-to-soil' in lines[i]:
        start_seed2soil = i+1

seed2soil = get_map([start_seed2soil, start_soil2fertilizer])
soil2fertilizer = get_map([start_soil2fertilizer, start_fertilizer2water])
fertilizer2water = get_map([start_fertilizer2water, start_water2light])
water2light = get_map([start_water2light, start_light2temperature])
light2temperature = get_map([start_light2temperature, start_temperature2humidity])
temperature2humidity = get_map([start_temperature2humidity, start_humidity2location])
humidity2location = get_map([start_humidity2location, len(lines)])

seed_ranges = get_seed_ranges(seeds)
seed_ranges = apply_destination_rules(seed_ranges, seed2soil)
seed_ranges = apply_destination_rules(seed_ranges, soil2fertilizer)
seed_ranges = apply_destination_rules(seed_ranges, fertilizer2water)
seed_ranges = apply_destination_rules(seed_ranges, water2light)
seed_ranges = apply_destination_rules(seed_ranges, light2temperature)
seed_ranges = apply_destination_rules(seed_ranges, temperature2humidity)
seed_ranges = apply_destination_rules(seed_ranges, humidity2location)

min_location = float('inf')
for range in seed_ranges:
    if range[1] < min_location:
        min_location = range[1]

print(min_location)
