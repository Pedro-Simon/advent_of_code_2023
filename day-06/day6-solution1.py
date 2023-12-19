import re

class Race():

    def __init__(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()
        self.time_list = re.split(r'\s+', lines[0].strip())[1:]
        self.distance_list = re.split(r'\s+', lines[1].strip())[1:]

    def get_num_wins(self, time, record_distance):
        times_winned = 0
        for hold_ms in range(int(time)+1):
            moving_ms = int(time) - hold_ms

            dist = moving_ms * hold_ms
            if dist > int(record_distance):
                # print(f'hold for {hold_ms} and moved for {moving_ms} ms, resulting in distance of {dist} (compared to the record {record_distance})')
                times_winned += 1
        return times_winned

    def calculate_races(self):
        total_wins = 1
        for i in range(len(self.time_list)):
            time = self.time_list[i]
            distance = self.distance_list[i]
            total_wins *= self.get_num_wins(time, distance)
        return total_wins

race = Race('input.txt')
print(race.calculate_races())
