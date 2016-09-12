def partition_alg_a(in_list, left, right):
    i = left
    j = right - 1

    while(True):
        while(in_list[i] <= in_list[left] and i < right - 1):
            i += 1
        while(in_list[j] >= in_list[left] and j > left):
            j -= 1

        if i < j:
            _swap(in_list, i, j)
        else:
            break

    _swap(in_list, left, j)
    return j

def partition_alg_b(in_list, left, right):
        i = left + 1
        for j in range(left + 1, right):
            if in_list[j] < in_list[left]:
                _swap(in_list, i, j)
                i += 1
        _swap(in_list, i - 1, left)
        return i - 1

def _swap(in_list, i, j):
    in_list[i], in_list[j] = in_list[j], in_list[i]

def quick_sort(in_list, left, right, partition_alg=partition_alg_a):

    def _select_pivot():
        return left

    if right - left <= 1:
        return

    pivot = _select_pivot()
    _swap(in_list, left, pivot)

    cut_point = partition_alg(in_list, left, right)

    quick_sort(in_list, left, cut_point)
    quick_sort(in_list, cut_point + 1, right)





