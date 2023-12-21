import re

class PipeWalker():
    def __init__(self, file_name):
        file = open(file_name, "r")
        self.map = [[char for char in line.strip()] for line in file.readlines()]

        self.start_pos = self.find_s()

        self.decoder = {
            'J':{'0,1':[-1,0], '0,-1':[], '1,0':[0, -1], '-1,0':[]},
            'L':{'0,1':[], '0,-1':[-1,0], '1,0':[0, 1], '-1,0':[]},
            'F':{'0,1':[], '0,-1':[1, 0], '1,0':[], '-1,0':[0, 1]},
            '7':{'0,1':[1,0], '0,-1':[], '1,0':[], '-1,0':[0, -1]},
            '|':{'0,1':[], '0,-1':[], '1,0':[1,0], '-1,0':[-1,0]},
            '-':{'0,1':[0,1], '0,-1':[0,-1], '1,0':[], '-1,0':[]},
            '.':{'0,1':[], '0,-1':[], '1,0':[], '-1,0':[]},
            'S':{'0,1':[], '0,-1':[], '1,0':[], '-1,0':[]}
        }
    
    def find_s(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'S':
                    return [y, x]
    
    def step(self, dir, pos):
        new_pos = [d + p for d, p in zip(dir, pos)]
        pipe_type = self.map[new_pos[0]][new_pos[1]]
        new_dir = self.decoder[pipe_type][",".join(map(str, dir))]
        return new_dir, new_pos
    
    def walk_trought(self):
        step_n = 0
        d_try = -1
        directions_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dir = []
        while True:
            if dir == []:
                # resets the starting position and changes the starting direction
                d_try += 1
                dir = directions_list[d_try]
                pos = self.start_pos
                # resets the x and y list
                x_list = []
                y_list = []
            dir, pos = self.step(dir, pos)

            x_list.append(pos[1])
            y_list.append(pos[0])
            step_n += 1
            if pos == self.start_pos:
                return x_list, y_list, step_n
            
    def x_ray(self):
        # 1 - substitute in the map the boundaries
        x_list, y_list, step_n = self.walk_trought()

        for x, y in zip(x_list, y_list):
            if self.map[y][x] == 'L' or self.map[y][x] == '7':
                self.map[y][x] = '$'
            elif self.map[y][x] != '7':
                self.map[y][x] = '@'

        inner_count = 0
            
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] != '@' and self.map[y][x] != '$':
                    y_move = y
                    x_move = x
                    n_boundaries = 0
                    while y_move < len(self.map) and x_move < len(self.map[y]):
                        if self.map[y_move][x_move] == '@':
                            n_boundaries += 1
                        y_move += 1
                        x_move += 1
                    if n_boundaries%2 != 0:
                        print(f'{y}, {x}, {self.map[y][x]}')
                        self.map[y][x] = 'I'
                        inner_count += 1
                    else:
                        self.map[y][x] = 'O'
        return inner_count

if __name__ == '__main__':
    Walker = PipeWalker('input.txt')
    print(Walker.x_ray())

    with open('output.txt', 'w') as file:
        for sublist in Walker.map:
            # Convert each element in the sublist to a string and join them with a delimiter (e.g., comma)
            line = ''.join(map(str, sublist))
            file.write(line + '\n')
