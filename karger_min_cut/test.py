import unittest
from utils import parse
from karger import karger

class TestKargerMinCut(unittest.TestCase):
    def test_sample_1(self):
        graph = parse('sample-1.txt')

        result = karger(graph)
        ans = 2

        self.assertEqual(ans, result)

    def test_sample_2(self):
        graph = parse('sample-2.txt')

        result = karger(graph)
        ans = 1

        self.assertEqual(ans, result)

if __name__ == '__main__':
    unittest.main()
