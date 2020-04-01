
from collections import deque
import numpy as np

# odd = deque()
# for i in range(10):
#     element = np.random.randint(10)
#     print(element)
#     odd.append(element)
#
# print(odd)
# print(odd.appendleft.__doc__)
# odd.appendleft(10000)
# print(odd)
# print(odd.pop())

def reorder_array(array):
    odd = list()
    length = len(array)
    for i in range(length):
        if array[length-i-1] %2 !=0:
            odd.insert(0,array[length-i-1])
        if array[i] % 2 == 0:
            odd.append(array[i])
        print("i: ",i)
        print(odd)

    return odd

array = [2,3,7,1,6,10]
odd = reorder_array(array)
print("odd: ", odd)