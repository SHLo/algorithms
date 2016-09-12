import sys
from math import floor

def main():
    try:
        in_file_name = sys.argv[1]
        out_file_name = sys.argv[2]
    except Exception:
        sys.stdout.write('Usage: python merge_sort.py'
                         '${in_file_name} ${out_file_name}\n')
        return

    in_list = []
    out_list = []

    with open(in_file_name) as source:
        for line in source:
            in_list.append(int(line))

    out_list, inv = merge_sort_count_inv(in_list)
    answer = sorted(in_list)
    if answer == out_list:
        print('correct!')
        print('inv %d' % inv)
    else:
        print('wrong!')


    with open(out_file_name, 'w') as target:
        for line in out_list:
            target.write('%s\n' % line)

def merge_sort_count_inv(in_list):
    if len(in_list) <= 1:
        return in_list, 0

    mid = int(floor(len(in_list) / 2))

    left_half, left_inv = merge_sort_count_inv(in_list[:mid])
    right_half, right_inv = merge_sort_count_inv(in_list[mid:])

    out_list, cross_inv = _merge_count_inv(left_half, right_half)

    return out_list, left_inv + right_inv + cross_inv

def _merge_count_inv(left_half, right_half):
    out_list = []

    i = 0
    j = 0
    inv = 0

    while(i < len(left_half) and j < len(right_half)):
        left = left_half[i]
        right = right_half[j]

        if left < right:
            out_list.append(left)
            i += 1
        else:
            out_list.append(right)
            j += 1
            inv += (len(left_half) - i)

    if i < len(left_half):
        out_list.extend(left_half[i:])
    elif j < len(right_half):
        out_list.extend(right_half[j:])

    return out_list, inv


if __name__ == '__main__':
    main()
