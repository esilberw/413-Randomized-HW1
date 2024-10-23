import math

import main
import random
import sys
import copy


def quick_select_bound_checking(length_list, comparison_counter):
    quick_select_bound = length_list * 3.386
    return comparison_counter < quick_select_bound


def lazy_select_bound_checking(length_list, comparison_counter):
    lazy_select_bound = length_list * 2 + length_list
    return comparison_counter < lazy_select_bound


def test_lazy_select():
    test_list, k = generator_array_k()
    copy_test_list = copy.deepcopy(test_list)
    copy_test_list.sort()
    lazy_select = main.RandomizedSelectionAlgo(test_list)
    selection = lazy_select.lazy_select(k)
    comparison_counter = lazy_select.comparison_counter

    try:
        assert selection == copy_test_list[k - 1]
        print("Test passed")
        print(lazy_select_bound_checking(len(test_list), comparison_counter))
    except AssertionError:
        print("Error Test Failed")
    print(lazy_select.lazy_select(k))
    print(lazy_select)


def test_quick_select():
    test_list, k = generator_array_k()
    copy_test_list = copy.deepcopy(test_list)
    copy_test_list.sort()
    quick_select = main.RandomizedSelectionAlgo(test_list)
    selection = quick_select.recursive_quick_select(0, len(test_list) - 1, k)
    comparison_counter = quick_select.comparison_counter
    try:
        assert selection == copy_test_list[k - 1]
        print("Test passed")
        print(quick_select_bound_checking(len(test_list), comparison_counter))
    except AssertionError:
        print("ERROR Test failed")
    return comparison_counter


def generator_array_k():
    generated_list = []
    generated_list_size = 10 ** 4

    for i in range(generated_list_size):
        new_elem = random.randrange(generated_list_size)

        while new_elem in generated_list:
            new_elem = random.randrange(generated_list_size)
        generated_list.append(new_elem)
    k = random.randint(0, generated_list_size)
    return generated_list, k


def average(list_of_numbers):
    return sum(list_of_numbers) // len(list_of_numbers)


def multiple_tests_quick_select():
    comparison_counter_list = []

    for i in range(100):
        try:
            comparison_counter_list.append(test_quick_select())
        except ValueError:
            print('ERROR')
    return average(comparison_counter_list)


def quick_select_bound_checking_average(average_comparison_counter):
    """
    :param average_comparison_counter: the average of the comparison counters of 100 tests with the quickselect algo
    :return: if the average comparison counter < quickselect bound, or not.
    """
    length = 10 ** 3
    return average_comparison_counter < length * 3.386, average_comparison_counter


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 8)
    in_average = quick_select_bound_checking_average(multiple_tests_quick_select())
    print(in_average)
