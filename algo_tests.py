import main
import random

class AlgoTest:
    def generator_array_k(self):
        generated_list = []
        generated_list_size = random.randrange(0, 10**4)
        for i in range(generated_list_size):
            new_elem = random.randrange(generated_list_size)
            if new_elem not in generated_list:
                generated_list.append(new_elem)
        k = random.choice(generated_list) # random choice of the element to find, sure is in the list
        print(k)
        return generated_list, k

    def test_quick_select(self):
        test_list, k = self.generator_array_k()
        print(test_list)
        print(k)
        quick_select = main.QuickSelect(test_list)
        quick_select.quick_select(0, len(test_list) -1, k)

algo_test = AlgoTest()
print(algo_test.test_quick_select())
