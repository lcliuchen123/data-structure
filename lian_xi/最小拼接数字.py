
from functools import cmp_to_key

def get_min_num(numbers):
    if not numbers:
        return ''

    lam = lambda x1,x2 : int(str(x1)+str(x2))  - int(str(x2)+str(x1))
    array = sorted(numbers,key=cmp_to_key(lam))
    ans = ''.join([str(i) for i in array])

    return ans

numbers = [3,32,321]
ans = get_min_num(numbers)
print(ans)