import sys
from utils import parse
from utils import Heap

def main():
    try:
        in_file_name = sys.argv[1]
    except Exception:
        sys.stderr.write('Usage: python median_maintenance.py ${in_file_name}')

    nums = parse(in_file_name)

    result = median_maintenance(nums)

    print(result)


def median_maintenance(nums):
    min_heap = Heap(min)
    max_heap = Heap(max)

    for num in nums:
        if max_heap.root() is None:
            max_heap.add(num)
        elif min_heap.root() is None:
            min_heap.add(num)
        elif num < max_heap.root():
            max_heap.add(num)
        else:
            min_heap.add(num)

        if (len(min_heap) - len(max_heap)) > 1:
            max_heap.add(min_heap.extract_root())
        elif (len(max_heap) - len(min_heap)) > 1:
            min_heap.add(max_heap.extract_root())

        if len(max_heap) > len(min_heap):
            result = max_heap.root()
        elif len(min_heap) > len(max_heap):
            result = min_heap.root()
        else:
            result = (max_heap.root() + min_heap.root()) / 2.0

    return result


if __name__ == '__main__':
    main()
