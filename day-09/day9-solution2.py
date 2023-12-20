import re

class OasisPredictor():
    def __init__(self, file_name):
        file = open(file_name, "r")
        self.lines = [line.strip().split(' ') for line in file.readlines()]

    def decompose(self, input_line):
        result_line = []
        for i in range(1, len(input_line)):
            result_line.append(int(input_line[i]) - int(input_line[i-1]))
        return result_line
    
    def get_single_prediction(self, line):
        diagonal_list = [int(line[0])]
        has_values = True
        # print(f'original line was: {line}')
        while has_values:
            result_line = self.decompose(line)
            diagonal_list.append(result_line[0])
            line = result_line
            has_values = len([1 for x in result_line if x != 0]) > 0

        old_item = 0
        for item in reversed(diagonal_list):
            old_item = - old_item + item
        # print(f'returned a diagonal {diagonal_list}\nand prediction {old_item}\n')
        return old_item
    
    def run_all_lines(self):
        total_prediction = []
        for line in self.lines:
            total_prediction.append(self.get_single_prediction(line))
        return sum(total_prediction)

if __name__ == '__main__':
    Predictor = OasisPredictor('input.txt')
    print(Predictor.run_all_lines())
