
# 编程1
def get_sequence(a,b,r):
    result = []
    for i in a:
        for j in b:
            if j >= i and j - i <= r:
                x = (i,j)
                result.append(x)
                break
            elif j > i:
                x = (i,j)
                result.append(x)
                break
    return result

# if __name__ == "__main__":
    # line = input()
    # a = [int(x) for x in line[3:8:2]]
    # b = [int(y) for y in line[13:18:2]]
    # r = int(line[-1])
    # result = get_sequence(a,b,r)
    # print(result)
    # ans = ''
    # for item in result:
    #     str_item =  '(' +str(item[0]) + ',' + str(item[1]) + ')'
    #     ans += str_item
    # print(ans)

# (1,2)(3,4)(5,6)
# (1, 2)(3, 4)(5, 6)


# 编程2
def is_eff(c):
    if (c >= 'a' and c <= 'z') or \
            (c >= 'A' and c <= 'Z') \
            or (c >= '0' and  c <= '9'):
        return True
    return False


line = input()
new_line = ''
count = 0
for i in range(len(line)):
    if line[i] == ' ':
        new_line += line[i]
    if is_eff(line[i]):
        new_line += line[i]
    elif line[i] == '-':
        if i - 1 >= 0 and is_eff(line[i - 1]) and i + 1 < len(line) and is_eff(line[i + 1]):
            new_line += line[i]
        count = 0
        while line[i] == '-':
            count += 1
            i += 1
        if count >= 2:
            new_line += ' '
print("new_line: ",new_line)
ans = ''
final_line = new_line.split()
length = len(final_line)
for i in range(length - 1, -1, -1):
    ans += final_line[i]
    ans += ' '

print(ans)


#3. 机票调整
n = int(input())
before = []
result = []
for i in range(n):
    before.append(input().split(',')[0])
    result.append(input())

m = int(input())
modify = []
for i in range(m):
    if input().split(',')[0] in before:
        modify.append(input())

print(modify)