
# 第一题：AC 每次删除不重复的两个数，是否能完全删完
# def get_result(number_list):
#     if number_list is None or len(number_list) == 0:
#         return
#     d = {}
#     mid = len(number_list)//2
#     for i in number_list:
#         d[i] = d.get(i,0)+1
#         if d.get(i)> mid:
#             return "NO"
#     return "YES"
#
# t = int(input())
# for k in range(t):
#     n = int(input())
#     number = input()
#     number_list = [int(x) for x in number.split()]
#     result = get_result(number_list)
#     print(result)


#第二题：求期望，抛n枚硬币，n:硬币数量，p:至少正面朝上的数量，q:至少反面朝上的数量
def get_ex(n,p,q):
    print([n,p,q])
    if p == n:
        result = (1000000007+(2**n)) // (n*(n+1))
        return result

    if q == n:
        return 0

    result = 0
    for i in range(p,n-q+1):
        result += i
    print(result)
    result = (1000000007 + (2**n)) // result
    return result

line = input()
n,p,q = [int(x) for x in line.split()]
result = get_ex(n,p,q)
print(result)