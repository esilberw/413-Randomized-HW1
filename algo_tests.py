import main
import random
import sys
import copy


def test_lazy_select():
    test_list, k = generator_array_k()
    lazy_select = main.RandomizedSelectionAlgo(test_list)
    print(lazy_select.lazy_select(k))
    print(lazy_select)


def test_quick_select():
    test_list, k = generator_array_k()
    copy_test_list = copy.deepcopy(test_list)
    copy_test_list.sort()
    quick_select = main.RandomizedSelectionAlgo(test_list)
    selection = quick_select.recursive_quick_select(0, len(test_list) - 1, k)
    try:
        assert selection == copy_test_list[k - 1]
        print("Test passed")
    except AssertionError:
        print("ERROR Test failed")
    return quick_select.comparison_counter


def generator_array_k():
    generated_list = []
    generated_list_size = 10 ** 2

    for i in range(generated_list_size):
        new_elem = random.randrange(generated_list_size)

        while new_elem in generated_list:
            new_elem = random.randrange(generated_list_size)
        generated_list.append(new_elem)
    k = random.randint(0, generated_list_size)
    return generated_list, k


def multiple_tests_quick_select():
    for i in range(100):
        test_quick_select()


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 8)
    print(test_quick_select())
