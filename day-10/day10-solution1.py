import re

class PipeWalker():
    def __init__(self, file_name):
        file = open(file_name, "r")
        self.map = [line.strip() for line in file.readlines()]

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
            dir, pos = self.step(dir, pos)

            step_n += 1
            if pos == self.start_pos:
                return step_n/2
            
        


if __name__ == '__main__':
    Walker = PipeWalker('test.txt')
    print(Walker.walk_trought())


# g[y][x]
# [-1, 1] OR [1, -1]