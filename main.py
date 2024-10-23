import math
import sys
import random


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

    def partition(self, low, high):
        """
        :param low: lower bound of the partition
        :param high: higher bound of the partition
        :return: the index of the actual random pivot after partitioning
        """""
        pivot_index = random.randint(low, high)

        # Move temporally the random pivot
        self.array[pivot_index], self.array[high] = self.array[high], self.array[pivot_index]
        random_pivot = self.array[high]

        i = low
        for j in range(low, high):
            if self.array[j] < random_pivot:    # sort all the element < pivot before the pivot
                self.comparison_counter += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i += 1

        self.array[i], self.array[high] = self.array[high], self.array[i]
        return i

    def recursive_quick_select(self, low, high, k):
        """
        :param low: lower bound of the partition
        :param high: upper bound of the partition
        :param k: the kth largest element of the array
        :return: the kth largest element
        """
        pivot_index = self.partition(low, high)

        if pivot_index == k - 1:  # if the element is found
            self.found_elem = self.array[pivot_index]
            self.index_elem = pivot_index
            self.quick_select_bound_checking()
            return pivot_index, self.array[pivot_index]

        elif pivot_index > k - 1:  # k is at the left of the pivot
            return self.recursive_quick_select(low, pivot_index - 1, k)

        else:   # k is at the right of the pivot
            return self.recursive_quick_select(pivot_index + 1, high, k)

    def rank_determination(self, x):
        rank_x = 1
        for elem in self.array:
            if elem < x:
                rank_x += 1
        return rank_x

    def lazy_select(self, k):
        """
        :param k: k-th smallest element in the array >< the element k in the array !
        :param k:
        :return:
        """
        P = []
        n_exp_3_4 = int(round(self.n ** (3/4)))  # need to convert in int for the forloop
        found_flag = False

        while not found_flag:
            index = 0
            random_pick_elems_R = []
            P = []

            for i in range(n_exp_3_4):
                new_random_pick = random.choice(self.array)
                while new_random_pick in random_pick_elems_R:
                    new_random_pick = random.choice(self.array)  # to ensure that we don't add an element already picked

                random_pick_elems_R.append(new_random_pick)

            random_pick_elems_R.sort()  # sort() use the timsort algo ==> O(n.log(n)), so optimal.

            x = k * self.n**(-1/4)

            l = max(math.floor(x - self.n**(1/2)), 0)
            h = min(math.ceil(x + self.n**(1/2)), n_exp_3_4 - 1)
            print(n_exp_3_4, random_pick_elems_R)
            print(l, h)

            a = random_pick_elems_R[int(l)]
            b = random_pick_elems_R[int(h)]

            rank_a_in_S = self.rank_determination(a)
            rank_b_in_S = self.rank_determination(b)

            if k < self.n ** (1/4):
                for y in range(self.n):
                    if self.array[y] <= b:
                        P.append(self.array[y])

                if k <= rank_b_in_S and len(P) <= (4 * self.n ** (3/4) + 2):
                    found_flag = True
                    index = k - rank_a_in_S + 1
                    self.found_elem = P[index]
                    self.index_elem = k

            elif k > int(self.n - self.n**(1/4)):
                for y in range(self.n):
                    if self.array[y] >= a:
                        P.append(self.array[y])

                if k >= rank_a_in_S and len(P) <= (4 * self.n ** (3/4) + 2):
                    found_flag = True
                    index = k - rank_a_in_S + 1
                    self.found_elem = P[index]
                    self.index_elem = k - rank_a_in_S + 1

            elif k in range(int(self.n**(1/4)), int((self.n - self.n**(1/4)) + 1)):  # +1 because of the range function
                for y in range(self.n):
                    if a <= self.array[y] <= b:
                        P.append(self.array[y])

                if rank_a_in_S <= k <= rank_b_in_S and len(P) <= (4 * self.n ** (3/4) + 2):
                    found_flag = True
                    index = k - rank_a_in_S + 1
                    self.found_elem = P[index]
                    self.index_elem = k - rank_a_in_S + 1

        P.sort()
        print(P, P[index], index)


sys.setrecursionlimit(10**8)  # to allow a bigger maximum recursion depth
test_list = [10, 14, 7, 8, 1, 3, 4, 2]
rando = RandomizedSelectionAlgo(test_list)
rando.lazy_select(3)
print(rando)