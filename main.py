import random
import sys

class QuickSelect:

    def __init__(self, array):
        self.array = array
        self.n = len(self.array)
        self.found_elem = -1
        self.index_elem = None

    def __repr__(self):
        return self.array

    def __str__(self):
        return "Tested_list: {}\nElement to find:{}\nIndex of the element:{}".format(self.array, self.found_elem, self.index_elem)
    def partition(self, low, high, random_pivot):
        print("random pivot:", random_pivot)
        i = low
        for j in range(low, high):
            if self.array[j] < random_pivot:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                print(self.array)
                i += 1
        print(self.array)
        return i

    def iterative_quick_select(self, k):
        low, high = 0, self.n - 1

        while low <= high:
            random_pivot = random.choice(self.array)
            pivot_index = self.partition(low, high, random_pivot)
            print(pivot_index, self.array, low, high)
            if self.array[pivot_index] == k:
                self.found_elem = self.array[pivot_index]
                self.index_elem = pivot_index
                return self.array[pivot_index], pivot_index


            elif k < self.array[pivot_index]:
                high = pivot_index - 1

            else:
                low = pivot_index + 1

        raise ValueError("! Element not found in the array, try another element ! ")
    def quick_select(self, low, high, k):
        pivot_index = self.partition(low, high)

        if self.array[pivot_index] == k: # if the element is found
            self.found_elem = self.array[pivot_index]
            self.index_elem = pivot_index
            return pivot_index, self.array[pivot_index]
        elif pivot_index > k:
            return self.quick_select(low, pivot_index - 1, k)
        else:
            return self.quick_select(pivot_index + 1, high, k)

    def lazy_selecy(self):
        return None

sys.setrecursionlimit(10**8) # to allow a bigger maximum recursion depth
tested_list =[48, 5, 20, 10, 7, 45, 15, 54, 41, 42, 30, 57, 31, 32, 37, 6, 19, 0, 26, 39, 40, 12, 25]
quick_select = QuickSelect(tested_list)
try:
    result = quick_select.iterative_quick_select(5)
    print(quick_select)
except ValueError as err:
    print(err)