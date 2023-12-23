import re
from itertools import permutations

class Repair():
    def __init__(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()
        
        self.repair_list = [line.strip().split(' ')[0] for line in lines]
        self.arr_list = [[int(arr) for arr in line.strip().split(' ')[1].split(',')] for line in lines]

        self.DP = {}


    def is_valid(self, solution, arr):
        # gets the input test and template and returns true if its valid
        test_list = re.split(r'\.+', solution)
        compare = [len(x) for x in test_list if x != '']
        if compare == arr:
            return 1
        return 0

    def recursive(self, repair, arr, i, nArr, nHash):
        # tests each part of the solution in a recursive way but using Dynamic programming
        key = (i, nArr, nHash)
        if key in self.DP:
            return self.DP[key]
        if i == len(repair):
            if nArr == len(arr) and nHash == 0:
                return 1
            elif nArr == len(arr) -1 and nHash == arr[nArr]:
                return 1
            else:
                return 0
        ans = 0
        # 2. Apply different solutions perspective, summing the possible solutions
        for c in ['.', '#']:
            if repair[i] == c or repair[i] == '?':
                if nHash == 0 and c == '.':
                    ans += self.recursive(repair, arr, i+1, nArr, nHash)
                elif nHash > 0 and c == '.' and nArr<len(arr) and nHash == arr[nArr]:
                    ans += self.recursive(repair, arr, i+1, nArr+1, 0)
                elif c == '#':
                    ans += self.recursive(repair, arr, i+1, nArr, nHash+1)
        # store solutions count for each key of DP
        self.DP[key] = ans
        return ans
    
    def check_true_combinations(self):
        ans = 0
        for repair, arr in zip(self.repair_list, self.arr_list):
            repair = '?'.join([repair, repair, repair, repair, repair])
            n_arr = arr.copy()
            for i in range(4):
                arr.extend(n_arr)

            self.DP.clear()
            ans += self.recursive(repair, arr, 0, 0, 0)
        return ans


if __name__ == '__main__':
    hRepair = Repair('input.txt')
    # print(dStar.sum_all_dists())
    print(hRepair.check_true_combinations())