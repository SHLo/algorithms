import unittest
from utils import parse_file
from scc import scc

class TestSCC(unittest.TestCase):
    def test_sample_1(self):
        graph = parse_file('sample-1.txt')
        result = scc(graph)
        answer = [3, 3, 3]

        self.assertEqual(result, answer)

    def test_sample_2(self):
        graph = parse_file('sample-2.txt')
        result = scc(graph)
        answer = [3, 3, 2]

        self.assertEqual(result, answer)

    def test_sample_5(self):
        graph = parse_file('sample-5.txt')
        result = scc(graph)
        answer = [6, 3, 2, 1]

        self.assertEqual(result, answer)
if __name__ == '__main__':
    unittest.main()
