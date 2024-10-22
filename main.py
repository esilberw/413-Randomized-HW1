import math
import random
import sys


class RandomizedSelectionAlgo:

    def __init__(self, array):
        self.array = array
        self.n = len(self.array)
        self.found_elem = -1
        self.index_elem = None
        self.comparison_counter = 0
        self.quick_select_bound_flag = False
        self.lazy_select_bound_flag = False

    def __repr__(self):
        return self.array

    def __str__(self):
        return ("Tested_list: {}\nSize of the list: {}\nElement to find: {}\nIndex of the element: {}\nNumber of "
                "comparison: {}\nBounded number comparisons: {}").format(self.array, self.n, self.found_elem, self.index_elem, self.comparison_counter, self.quick_select_bound_flag)

    def quick_select_bound_checking(self):
        quick_select_bound = self.n * 3.386
        if self.comparison_counter < quick_select_bound:
            self.quick_select_bound_flag = True

    def lazy_select_bound_checking(self):
        lazy_select_bound = self.n * 2
        if self.comparison_counter < lazy_select_bound:
            self.lazy_select_bound_flag = True

    def partition(self, low, high, random_pivot):
        i = 0

        for j in range(low, high):
            if self.array[j] < random_pivot:    # sort all the element < pivot before the pivot
                self.comparison_counter += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i += 1

        pivot_index = self.array.index(random_pivot)
        self.array[pivot_index], self.array[i] = self.array[i], self.array[pivot_index]  # move pivot at index i
        return i

    def recursive_quick_select(self, low, high, k):

        random_pivot = random.choice(self.array)
        pivot_index = self.partition(low, high, random_pivot)

        if self.array[pivot_index] == k:  # if the element is found
            self.found_elem = self.array[pivot_index]
            self.index_elem = pivot_index
            self.quick_select_bound_checking()
            return pivot_index, self.array[pivot_index]
        elif pivot_index > k:  # k is at the left of the pivot
            return self.recursive_quick_select(low, pivot_index - 1, k)
        else:   # k is at the right of the pivot
            return self.recursive_quick_select(pivot_index + 1, high, k)


    def rank_determination(self, x):
        rank_x = 0
        for elem in self.array:
            print("TAMERE")
        return rank_x

    def lazy_select(self, k):
        n_exp_3_4 = int(self.n ** (3/4)) # need to convert in int for the forloop
        random_pick_elems_R = []
        P = []
        a, b = 0, 0

        while k not in P and len(P) >= 4*self.n**3/4 + 2:
            for i in range(n_exp_3_4):
                new_random_pick = random.choice(self.array)
                while new_random_pick not in random_pick_elems_R:
                    random_pick_elems_R.append(new_random_pick) # to ensure that we don't add an element already picked

            random_pick_elems_R.sort() # sort() use the timsort algo ==> O(n.log(n)), so optimal.

            x = k*self.n**(-1/4)
            l = max(math.floor(x - math.sqrt(self.n)), 1)
            h = min(math.ceil(x + math.sqrt(self.n)), n_exp_3_4)

            a = random_pick_elems_R[l]
            b = random_pick_elems_R[h]
            rank_a_in_S = self.rank_determination(a)
            rank_b_in_S = self.rank_determination(b)

            if k < self.n ** 1/4:
                for y in range(self.n):
                    if self.array[y] <= b:
                        P.append(self.array[y])

            elif k > self.n - self.n**1/4:
                for y in range(self.n):
                    if self.array[y] >= a:
                        P.append(self.array[y])

            elif k in range(self.n**1/4, self.n - self.n**1/4):
                for y in range(self.n):
                    if a <= y <= b:
                        P.append(y)
        P.sort()
        self.found_elem = P[k - self.array[a]+ 1]
        return P[k - a + 1]


sys.setrecursionlimit(10**8)  # to allow a bigger maximum recursion depth
test_list = [1,3, 4, 2, 10, 14, 7]
rando = RandomizedSelectionAlgo(test_list)
rando.lazy_select(2)
print(rando)