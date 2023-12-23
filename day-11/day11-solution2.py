import re
from itertools import combinations


class StarDist():
    def __init__(self, file_name):
        file = open(file_name, "r")
        self.universe_map = [[char for char in line.strip()] for line in file.readlines()]
        
        temp_galaxies = self.get_coordenates()

        self.galaxies = self.expand_map(temp_galaxies)

    def expand_map(self, temp_galaxies):
        y_lenght = len(self.universe_map)
        x_lenght = len(self.universe_map[0])
        add_rows = []
        add_columns = []
        
        for y, line in enumerate(reversed(self.universe_map)):
            if '#' not in line:
                Y = y_lenght -1 - y
                add_rows.append(Y)            

        for x in range(len(self.universe_map[0])):
            X = x_lenght -1 - x
            if '#' not in [line[X] for line in self.universe_map]:
                add_columns.append(X)

        add_rows = [sum([1 for y in add_rows if x >= y]) for x in range(y_lenght)]
        add_columns = [sum([1 for y in add_columns if x >= y]) for x in range(x_lenght)]

        expand_factor = 10**6-1
        temp_galaxies = [(line[0],line[1] + add_rows[line[1]]*expand_factor) for line in temp_galaxies]
        temp_galaxies = [(line[0] + add_columns[line[0]]*expand_factor,line[1]) for line in temp_galaxies]

        return temp_galaxies
    
    def get_coordenates(self):
        coord = []
        for y, line in enumerate(self.universe_map):
            for x, value in enumerate(line):
                if value == '#':
                    coord.append((x, y))
        return coord
    
    def get_dist(self, gal1, gal2):
        x1 = gal1[0]
        y1 = gal1[1]
        x2 = gal2[0]
        y2 = gal2[1]

        return abs(x2 - x1)+abs(y2 - y1)
    
    def get_combinations(self):
        return list(combinations(self.galaxies, 2))

    def sum_all_dists(self):
        sum_dists = 0
        comb_list = self.get_combinations()

        for comb in comb_list:
            dist = self.get_dist(comb[0], comb[1])
            sum_dists += dist
    
        return sum_dists
if __name__ == '__main__':
    dStar = StarDist('input.txt')
    print(dStar.sum_all_dists())