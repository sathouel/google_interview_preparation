import unittest
import random
from quick_sort import sort as quick_sort
from merge_sort import sort as merge_sort

class TestSort(unittest.TestCase):
        def setUp(self):
            start, end, length, times = 1, 10000, 250, 1000
            self.random_lists = [[random.randint(start, end) for _ in range(length)] for _ in range(times)]

        def testQuickSort(self):
            for lst in self.random_lists:
                true_sorted_list = sorted(lst)
                my_sorted_list = quick_sort(lst)
                error_message = 'true {} / wrong {}'.format(true_sorted_list, my_sorted_list)
                self.assertListEqual(true_sorted_list, my_sorted_list, msg=error_message)

        def testMergeSort(self):
            for lst in self.random_lists:
                true_sorted_list = sorted(lst)
                my_sorted_list = merge_sort(lst)
                error_message = 'true {} / wrong {}'.format(true_sorted_list, my_sorted_list)
                self.assertListEqual(true_sorted_list, my_sorted_list, msg=error_message)                

if __name__ == '__main__':
    unittest.main()
        