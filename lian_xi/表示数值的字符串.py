

# 解法一
def isNumeric(s):
    # write code here
    if not s:
        return False
    # 先判断整数
    count = 0
    num = 0
    for i in range(len(s)):
        if i == 0 and s[i] in ['+', '-']:
            continue
        # 科学计数法
        if s[i - 1] in ['e', 'E'] and s[i] in ['+', '-']:
            continue
        if s[i] in ['e', 'E']:
            count += 1
            if count > 1 or i+1 == len(s): #12e不是数字
                return False
            else:
                continue
        # 小数点
        if i > 0 and s[i] == '.':
            num += 1
            if num > 1:
                return False
            elif count > 0 and num >0:
                return False
            else:
                continue
        if s[i] < '0' or s[i] > '9':
            return False

    return True


# 解法二
def is_number(s):
    try:
        x = float(s)
        return True
    except:
        return False


if  __name__ == "__main__":
    s = '1a3.14'
    res =isNumeric(s)
    print(res)