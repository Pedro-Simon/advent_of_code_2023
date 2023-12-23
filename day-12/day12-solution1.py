import re
from itertools import permutations

class Repair():
    def __init__(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()
        
        self.repair_list = [line.strip().split(' ')[0] for line in lines]
        self.arr_list = [[int(arr) for arr in line.strip().split(' ')[1].split(',')] for line in lines]


    def is_valid(self, solution, arr):
        # gets the input test and template and returns true if its valid
        test_list = re.split(r'\.+', solution)
        compare = [len(x) for x in test_list if x != '']
        if compare == arr:
            return 1
        return 0

    def recursive(self, repair, arr, i):
        # tests each part of the solution in a recursive way

        # 3. If ended the matching, try the valid solution
        if i == len(repair):
            return self.is_valid(repair, arr)

        # 2. Apply different solutions perspective
        elif repair[i] == '?':
            return (self.recursive(repair[:i]+'.'+repair[i+1:], arr, i) + self.recursive(repair[:i]+'#'+repair[i+1:], arr, i))

        # 1. If non conditions matched, test the i+1 function
        else:
            return self.recursive(repair, arr, i+1)

    # def get_combinations(self, repair, arr):
    #     n_broken = sum([1 for i in repair if i == '#'])
    #     n_question = sum([1 for j in repair if j == '?'])
    #     n_template = sum([int(k) for k in arr])
        
    #     comb_input = ''.join(['#'*(n_template - n_broken), '.'*(n_question - (n_template - n_broken))])
    #     comb_list = set(permutations(comb_input, len(comb_input)))

    #     comb_list = [i for i in set(comb_list)]

    #     combinations = []
 
    #     for comb in comb_list:
    #         n = 0
    #         comb = [x for x in comb]
    #         new_string = ''.join([x if x != '?' else comb.pop() for x in repair ])
    #         combinations.append(new_string)
    #     return combinations
    
    def check_true_combinations(self):
        ans = 0
        for repair, arr in zip(self.repair_list, self.arr_list):
            ans += self.recursive(repair, arr, 0)
        
        return ans


if __name__ == '__main__':
    hRepair = Repair('input.txt')
    # print(dStar.sum_all_dists())
    print(hRepair.check_true_combinations())