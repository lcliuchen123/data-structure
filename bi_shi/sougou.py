
def get_sub_num(x,index):
    if index < 3:
        return 1
    if  x < 2:
        return 0
    num = 0

    for k in range((x-1)/2,x):
        sub_index = index - 1
        sub_num = get_sub_num(k,sub_index)
        num += sub_num

    return num

# x = int(input())
x = 3
d = {}
d[3] = x -1
j =4
while j > 3:
    number = get_sub_num(x, j)
    print("number: ", number)
    if number == 0:
        break
    d[j] = number
    print(d[j])
    j += 1

for k,v in d.items():
    print("%d %d" %(k,v))