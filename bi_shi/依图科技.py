
#
# def print_water(line):
#     n,m,a,b,c = [int(x) for x in line.split()]
#     for i in range(n):
#         num = [0] * m
#         for j in range(m):
#             tmp = abs(i-a)+abs(j-b)
#             num[j] = c - tmp
#             if num[j] < 0:
#                 num[j] = 0
#             print(num[j],end = ' ')
#         print()
#
# exa = int(input())
# for i in range(exa):
#     line = input()
#     print("Case #%d:" % (i+1))
#     print_water(line)
#

# 第二题
def get_reverse(A):
    A_T = []
    n,m = len(A),len(A[0])
    if n == 0 or m == 0:
        return A

    for i in range(m):
        tmp =[]
        for j in range(n):
            tmp.append(A[j][i])
        A_T.append(tmp)

    return A_T


def get_mult(A,B):
    C = []
    n = len(A)
    m = len(B[0])
    print(B)
    B_T = get_reverse(B)
    for i in range(n):
        tmp = []
        for j in range(m):
            a = A[i]
            b = B_T[j]
            # print(a)
            print(b)
            mul = sum([aa*bb for aa,bb in zip(a,b)])
            tmp.append(mul)
        C.append(tmp)

    return C


if __name__ == "__main__":
    line = input()
    n,m = [int(x) for x in line.split()]
    A= []
    B = []
    for i in range(2*n):
        line = input()

        tmp = [int(x) for x in line.split()]
        if i < n:
            A.append(tmp)
        else:
            B.append(tmp)
    # print(A)
    a_t = get_reverse(A)
    print("a_t: ",a_t)
    c = get_mult(a_t,B)
    print(c)
    b_t = get_reverse(B)
    ct = get_mult(c,b_t)
    res = get_reverse(ct)
    print("%d %d" %(len(res),len(res[0])))
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(res[i][j],end= ' ')
        print()
