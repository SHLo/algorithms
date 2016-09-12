import math
import sys
#import urllib.request


#for line in f:
    #print(line)

inp = []

with urllib.request.urlopen('http://spark-public.s3.amazonaws.com/algo1/programming_prob/QuickSort.txt') as f:
    for line in f:
        inp.append(int(line))

inp2 = inp[:]
def qs(inp, start, end, p_stgy):
    if not start < end:
        return 
    #print(inp)
    global comp
    comp += (end - start)
    if p_stgy == 'first':
        p = start
    elif p_stgy == 'last':
        p = end
    else:
        mid = int(math.floor((start + end) / 2))
        """
        mid_val = min(max(inp[start], inp[end]), inp[mid])
        if mid_val == inp[start]:
            p = start
        elif mid_val == inp[end]:
            p = end
        else:
            p = mid
        """ 
        if inp[mid] > inp[start] > inp[end] or inp[end] > inp[start] > inp[mid]:
            p = start
        elif inp[start] > inp[mid] > inp[end] or inp[end] > inp[mid] > inp[start]:
            p = mid
        else:
            p = end
        
        #print('mid: ', inp[p])


    inp[start], inp[p] = inp[p], inp[start]

    p_val = inp[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if inp[j] < p_val:
            inp[i], inp[j] = inp[j], inp[i]
            i += 1
    i -= 1
    inp[start], inp[i] = inp[i], inp[start]

    qs(inp, start, i - 1, p_stgy)
    qs(inp, i + 1, end, p_stgy)



comp = 0
p_stgy = sys.argv[1]

inp.sort()
qs(inp2, 0, len(inp2) - 1, p_stgy)

for i, (a, b) in enumerate(zip(inp, inp2)):
    if not a == b:
        print('wrong')
        break
else:
    print('correct')


print(comp)
#qs([1, 4, 7, 3, 6, 9], 0, 5, 'mid')
