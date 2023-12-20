import re

class MapManager():
    def __init__(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()

        self.directions = lines[0].strip().replace('R', '1').replace('L', '0')
        self.routes = {
            x.split(' = (')[0].strip(): 
            x.split(' = (')[1].replace(')', '').strip().split(', ') 
            for x in lines[2:]
        }

    def step(self, source, direction):
        return self.routes[source][int(direction)]
    
    def follow_map(self):
        n_steps = 0
        source = 'AAA'
        while source != 'ZZZ':
            d_step = n_steps%(len(self.directions))
            source = self.step(source, self.directions[d_step])
            n_steps += 1
        return n_steps

if __name__ == '__main__':
    Manager = MapManager('input.txt')
    print(Manager.follow_map())