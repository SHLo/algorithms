import sys

file_name = sys.argv[1]

nums = []

with open(file_name) as f_handle:
    for line in f_handle:
        num = int(line)
        nums.append(num)

    

rec = set(nums)

def two_sum(t):
    for num in rec:
        if t - num in rec:
            if not t == 2 * num:
                return 1
    return 0

ans = 0

for i in range(-10000, 10001, 1):
    ans += two_sum(i)


        
    


print(ans)
