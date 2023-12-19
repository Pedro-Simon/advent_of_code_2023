import re
import pandas as pd

file = open("input.txt", "r")
lines = file.readlines()
seeds = re.split(r'\s+', lines[0][7:].strip())

def get_map(ranges):
    df = pd.DataFrame(columns=['destination_start', 'source_start', 'range'])
    for i in range(ranges[0], ranges[1]-1):
        if not lines[i].strip() == '':
            new_row = lines[i].strip().split(' ')
            df.loc[len(df)] = new_row
            final_df = df.astype(int)
    return final_df

def find_destination(map, input):
    map['source_last'] = map['source_start'] + map['range']
    conversion_row = map[(map['source_start'].astype(int)<=int(input)) & (map['source_start'].astype(int) + map['range'].astype(int) >= int(input))]
    if len(conversion_row) > 0:
        result = conversion_row['destination_start'].astype(int).values[0] + (int(input) - conversion_row['source_start'].astype(int).values[0])
    else:
        result = input
    return result
    

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

min_location = float('inf')
for seed in seeds:
    soil = find_destination(seed2soil, seed)
    fertilizer = find_destination(soil2fertilizer, soil)
    water = find_destination(fertilizer2water, fertilizer)
    light = find_destination(water2light, water)
    temperature = find_destination(light2temperature, light)
    humidity = find_destination(temperature2humidity, temperature)
    location = find_destination(humidity2location, humidity)
    min_location = min(min_location, location)

print(min_location)
    