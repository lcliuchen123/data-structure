
# 自己的解法
def MoreThanHalfNum_Solution(numbers):
    # 判断是否为空
    if not numbers:
        return 0
    #判断个数是否为1
    if len(numbers)==1:
        return numbers[0]

    result = numbers[0]
    count = 1
    for i in range(1, len(numbers)):
        if numbers[i] != result:
            count -= 1
        else:
            count += 1
        if count == 0:
            result = numbers[i]
            count += 1
        # 判断是否大于n/2，如果大于直接返回
        if count > len(numbers) / 2:
            return result
    print(count)
    if count > 1:
        return result
    else:
        return 0


# 优化后的解法
def  get_zhongshu(numbers):
    if not numbers:
        return 0

    result = numbers[0]
    count = 1
    for i in range(1,len(numbers)):
        if numbers[i] == result:
            count += 1
        else:
            count -= 1

        if count == 0:
            result = numbers[i]
            count = 1

    count = 0
    for j in numbers:
        if result == j:
            count += 1

    if count > len(numbers)/2:
        return result
    else:
        return 0

numbers = [1,2,3,2,2,2,5,4,2]

# 解法三，使用模块
from collections import Counter
def get_result(numbers):
    if not numbers:
        return 0
    # 返回每个元素及对应的频数，可以选择前几个，most_common(n)
    counter = Counter(numbers).most_common()
    if counter[0][1] > len(numbers)//2:
        return counter[0]
    else:
        return 0

# result = MoreThanHalfNum_Solution(numbers)
result = get_zhongshu(numbers)
print(result)