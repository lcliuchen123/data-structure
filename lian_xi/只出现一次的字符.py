

def FirstNotRepeatingChar(s):
    from collections import Counter
    if not s or s=='':
        return -1
    s = [x for x in s]
    d = Counter(s)
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1

print(FirstNotRepeatingChar('google'))