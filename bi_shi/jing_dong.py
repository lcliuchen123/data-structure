
# 一、选择题
# 1.SQL:
# 1.1数据库的索引什么时候起作用，like 'aa%',只有在%后置时起作用
# 1.2SQL调优的方法：把having替换为where
# 2.哈夫曼树有5个叶节点，一共有多少个节点？
# 3.二叉树的先序、中序和后序遍历，二叉平衡树
# 4.Aprior算法的优化
# 5.凸集的定义
# 6.过滤器类型的特征选择有哪些？
# 7.Excel的if函数，if(A1>20,"合格","不合格")
# 8.方差和偏差
# 深度学习调优SGD，随机梯度下降

# 二、编程题
# 第一题：没有仔细思考，努努力可以ac，但是没有耗费时间在本地测试。
# 纠结点：1.如何对自己字典排序？2.如何生成value为列表的字典，key:姓，value：所有以key为姓的列表
# 错误1：自定义函数排序，遗忘了functools模块,sorted()函数，functools.cmp_To_key()
# 错误2：直接利用默认值为[]进行append报错，应先判断是否为空，如果为空，赋值列表；如果不为空直接append。
# 错误3：items()函数漏加括号
# 错误4：name误写为name[0]，输入不对

import functools

def compare(a,b):
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        return 0


def sort_name(name_list):
    name_count_dict = {}
    name_dict = {}
    for name in name_list:
        # print("name: ",name)
        count = 0
        xing = name.split()[0]
        # print("xing: ",xing)
        name_count_dict[xing] = name_count_dict.get(xing,0)+1
        if  not name_dict.get(xing):
            name_dict[xing] = [name]
        else:
            name_dict.get(xing).append(name)
    new_list = list(name_count_dict.items())
    # print("name_dict: ",name_dict)
    sorted_list = sorted(new_list,key=functools.cmp_to_key(compare))
    for item in sorted_list:
        # print(name_dict[item[0]])
        if len(name_dict[item[0]])>1:
            for name in name_dict[item[0]]:
                print(name)
        else:
            print(name_dict[item[0]])
name_list=[]
while True:
    import sys
    line = sys.stdin.readline().strip()
    if not line:
        break
    name_list.append(line)
print(name_list)
sort_name(name_list)


# 在英文的输入中，我们经常会遇到大小写切换的问题，
# 频繁切换大小写会增加我们的按键次数，也会降低我们的打字效率。
# 众所周知，切换大小写有两种方式，一种是按下“caps locks”，也就是大写锁定键，
# 这样一来，之后的输入模式都会被切换。另一种是同时按下shift和需要打印的字母，
# 可以临时切换大小写(算作按下两个键)。 已知初始状态下，打字模式是小写，
# 现在给出需要打印的字符串(区分大小写)，请你计算出最少需按键多少次才能打印出来。
# AC 0.18

def get_min_number(n,string):
    if n==0:
        return 0
    number = 1
    flag = True
    if string[0] >= 'A' and string[0]<= 'Z':
        flag = False
        number =2
    for i in range(1,n):
        if flag:
            if string[i] >= 'a' and string[i] <= 'z':
                number += 1
            else:
                flag= False
                number += 2
        else:
            if string[i] >= 'a' and string[i] <= 'z':
                number += 2
            else:
                flag = False
                number += 1
    return number



if __name__ == "__main__":
    import sys
    line =sys.stdin.readline().strip()
    n = int(line)
    string = sys.stdin.readline().strip()
    count = get_min_number(n,string)
    print(count)

