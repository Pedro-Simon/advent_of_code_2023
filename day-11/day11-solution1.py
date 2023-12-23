import re
from itertools import combinations


class StarDist():
    def __init__(self, file_name):
        file = open(file_name, "r")
        input_map = [[char for char in line.strip()] for line in file.readlines()]
        self.universe_map = self.expand_map(input_map)
        self.galaxies = self.get_coordenates()

    def expand_map(self, input_map):
        y_lenght = len(input_map)-1
        x_lenght = len(input_map[0])-1
        
        for y, line in enumerate(reversed(input_map)):
            if '#' not in line:
                Y = y_lenght - y
                input_map.insert(Y, input_map[Y])               

        for x in range(len(input_map[0])):
            X = x_lenght - x
            if '#' not in [line[X] for line in input_map]:
                for line in input_map:
                    line.insert(X, '.')
        return input_map
    
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