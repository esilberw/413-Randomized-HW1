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

    def lazy_select(self):
        return None


sys.setrecursionlimit(10**8)  # to allow a bigger maximum recursion depth
