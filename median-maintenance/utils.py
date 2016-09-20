import sys

def parse(file_name):
    nums = []
    with open(file_name) as lines:
        for line in lines:
            nums.append(int(line))
    return nums

class Heap():
    def __init__(self, select):
        self.nums = []
        self.select = select

    def __len__(self):
        return len(self.nums)

    def root(self):
        _root = None
        if len(self.nums):
            _root = self.nums[0]
        return _root

    def add(self, num):
        nums = self.nums
        nums.append(num)

        self._up_heapify(len(nums) - 1)

    def _up_heapify(self, pos):
        nums  = self.nums
        select = self.select

        if pos == 0:
            return

        parent = (pos - 1) / 2

        if select(nums[pos], nums[parent]) != nums[parent]:
            self._swap(pos, parent)
            self._up_heapify(parent)

    def _swap(self, pos_1, pos_2):
        nums = self.nums
        nums[pos_1], nums[pos_2] = nums[pos_2], nums[pos_1]

    def extract_root(self):
        nums = self.nums

        root = nums[0]
        nums[0] = nums.pop()
        self._down_heapify(0)

        print('extract_root: ', nums)
        return root

    def _down_heapify(self, pos):
        nums = self.nums
        select = self.select

        left = pos * 2 + 1
        right = pos * 2 + 2

        if pos >= len(nums) / 2:
            return
        elif left == len(nums) - 1:
            candidate = left
        else:
            if select(nums[left], nums[right]) == nums[left]:
                candidate = left
            else:
                candidate = right

        if select(nums[candidate], nums[pos]) != nums[pos]:
            self._swap(candidate, pos)
            self._down_heapify(candidate)


