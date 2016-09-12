import unittest
from quick_sort import quick_sort
from quick_sort import partition_alg_a
from quick_sort import partition_alg_b

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.in_list = []

        with open('QuickSort.txt') as lines:
            for line in lines:
                self.in_list.append(int(line))

        self.answer = sorted(self.in_list)

    def test_quick_sort_partition_a(self):
        out_list = self.in_list[:]
        quick_sort(out_list, 0, len(out_list), partition_alg_a)
        self.assertSequenceEqual(out_list, self.answer)

    def test_quick_sort_partition_b(self):
        out_list = self.in_list[:]
        quick_sort(out_list, 0, len(out_list), partition_alg_b)
        self.assertSequenceEqual(out_list, self.answer)

if __name__ == '__main__':
    unittest.main()
