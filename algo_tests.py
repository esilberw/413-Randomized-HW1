import threading

import main
import random
import sys


class AlgoTest:

    def generator_array_k(self):
        generated_list = []
        generated_list_size = 10**3
        for i in range(generated_list_size):
            new_elem = random.randrange(generated_list_size)
            while new_elem in generated_list:
                new_elem = random.randrange(generated_list_size)
            generated_list.append(new_elem)
        k = random.choice(generated_list)  # random choice of the element to find, sure is in the list
        return generated_list, k

    def test_quick_select(self):
        test_list, k = self.generator_array_k()
        quick_select = main.RandomizedSelectionAlgo(test_list)
        quick_select.recursive_quick_select(0, len(test_list) - 1, k)
        print(quick_select)

    def test_lazy_select(self):
        test_list, k = self.generator_array_k()
        lazy_select = main.RandomizedSelectionAlgo(test_list)
        print(lazy_select.lazy_select())
        print(lazy_select)


if __name__ == '__main__':
    sys.setrecursionlimit(10**8)
    threading.stack_size(200000000)
    algo_test = AlgoTest()
    algo_test.test_lazy_select()
