from functools import reduce
import math

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
    
    def simultaneous_step(self, sources_list, direction):
        all_z = False
        destinations_list = []
        for i in range(len(sources_list)):
            source = self.step(sources_list[i], direction)
            if source.endswith('Z'):
                all_z = True
            else:
                destinations_list.append(source)
        return destinations_list, all_z

    def calculate_lcm(self, a, b):
        return abs(a * b) // math.gcd(a, b)

    def lcm_of_list(self, numbers):
        return reduce(self.calculate_lcm, numbers)

    def follow_map(self):
        n_steps = 0
        cycle_list = []
        sources_list = [k for k, v in self.routes.items() if k[2] == 'A']

        while len(sources_list) > 0:
            d_step = n_steps%(len(self.directions))
            sources_list, all_z = self.simultaneous_step(sources_list, self.directions[d_step])
            n_steps += 1

            if all_z:
                cycle_list.append(n_steps)

        return self.lcm_of_list(cycle_list)

if __name__ == '__main__':
    Manager = MapManager('input.txt')
    print(Manager.follow_map())