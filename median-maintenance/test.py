import unittest
from utils import parse
from median_maintenance import median_maintenance

class TestMedianMaintenance(unittest.TestCase):
    def test_10(self):
        ans = -8448

        nums = parse('test10.txt')
        result = median_maintenance(nums)

        self.assertEqual(ans, result)

if __name__ == '__main__':
    unittest.main()
