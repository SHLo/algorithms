import unittest
from merge_sort import merge_sort_count_inv

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.in_list = []

        with open('IntegerArray.txt') as source:
            for line in source:
                self.in_list.append(int(line))

        self.answer = sorted(self.in_list)

    def test_merge_sort(self):
        out_list, _ = merge_sort_count_inv(self.in_list)
        self.assertSequenceEqual(out_list, self.answer)

if __name__ == '__main__':
    unittest.main()

