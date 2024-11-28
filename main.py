from itertools import permutations
import math

def make_pairs_lists(n):
    for i in range(0, 2 * n, 2): 
        brothers_list[i] = math.ceil((i + 1)/2)
    for i in range(1, 2 * n, 2): 
        brothers_list[i] = -(math.ceil((i + 1)/2))
    for i in range(0, 2 * n, 2): 
        sister_list[i] = math.ceil((i + 1)/2)
    for i in range(1, 2 * n, 2): 
        sister_list[i] = -(math.ceil((i + 1)/2))

def find_valid_perms():
    count = 0
    perms = permutations(sister_list)
    for perm in perms:
        is_valid = True
        for i in range(0, 2 * n, 2): 
            if (perm[i] == -(perm[i+1])):
                is_valid = False
        if (is_valid):
            # print (perm)
            count += 1
    return count

n = int (input ("How many pairs? "))
brothers_list = [0] * 2 * n
sister_list = [0] * 2 * n
make_pairs_lists(n)
print(brothers_list)
print(find_valid_perms())
