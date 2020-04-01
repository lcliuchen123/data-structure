
# line =input()
# line = [int(x) for x in line.split(',')]
# line = sorted(line)
# print(line)
# print(line[1])

def get_cishu(n):
    if n == 0:
        return 0
    ci_shu = [1,2]
    if n <= 2:
        return ci_shu[n-1]
    for i in range(2,n):
        f = ci_shu[-1] + ci_shu[-2]
        ci_shu.append(f)
        print(ci_shu)
    return ci_shu[-1]

n = int(input())
res = get_cishu(n)
print(res)