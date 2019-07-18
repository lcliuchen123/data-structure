
#各种位运算  &: 与 ^: 异或 相同为0，不同为1  >>:右移

def count_one(n):
    """count the number of 1 in binary of n
       n >> i :右移i位
       (n >> i) & 1: 判断第i为是否为1
    """

    return sum( (n >> i) & 1 for i in range(0,32))


def remove_last_one(n):
    """delete the last 1 in binary of n"""
    return n-1 & n

def is_multi_of2(n):
    """O(1) if n % 2 == 0: binary only have one 1"""
    return n & n-1


def search_only_once(number_list):
    """only one ,others appear twice"""
    count = 0
    for i in number_list:
        count = i ^ count

    return count


def search_only_once3(number_list):
    """only one, others appear third"""
    result = 0
    for i in range(32):
        count = 0
        for number in number_list:
            count += (number >> i) & 1
        if count % 3 == 1:
            result += 1 << i    #?????????????相当于在满足条件的二进制位上加入1
            print("i: ", i)
            print("result: ", result)

    return result


if __name__ == "__main__":
    l= [4,4,1,2,2,5,5]
    print(search_only_once(l))
    lis = [1,1,5,3,5,5,1,2,2,2]
    print(search_only_once3(lis))