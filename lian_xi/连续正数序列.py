
# 等差数列和：sum =（2a+n-1)*n/2
# 等比数列和：sum = a1(1-q^n)/(1-q)
def FindContinuousSequence(tsum):
    result = []
    for a in range(1, tsum):
        print("a: ",a)
        for n in range(1, tsum):
            print(n)
            t_sum = n * (2 * a + n - 1)
            print("t_sum: ", t_sum)
            if  t_sum == (2 * tsum):
                print("true")
                result.append([a + i for i in range(n)])
                print(result)

    return result

print(FindContinuousSequence(3))