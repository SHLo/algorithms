import unittest
import dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        pass

    def test_sample_1(self):
        answer = {
            '1': {
                'length': 0,
                'path': []
            },
            '2': {
                'length': 3,
                'path': ['2']
            },
            '3': {
                'length': 3,
                'path': ['3']
            },
            '4': {
                'length': 5,
                'path': ['2', '4']
            }
        }

        graph = dijkstra.parse_in_file('sample-1.txt')
        output = dijkstra.dijkstra(graph)
        self.assertEqual(answer, output)

    def test_medium_size(self):
        answer = 5

        graph = dijkstra.parse_in_file('medium-size.txt')
        output = dijkstra.dijkstra(graph)
        self.assertEqual(answer, output['7']['length'])

if __name__ == '__main__':
    unittest.main()
