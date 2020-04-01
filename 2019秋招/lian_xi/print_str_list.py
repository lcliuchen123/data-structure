
# 递归算法
def Permutation(string):
    if not string:
        return
    str_list=[]
    perm(string,str_list,'')
    unique = list(set(str_list))
    return sorted(unique)


def perm(ss,res,path):
    if ss=='':
        res.append(path)
    for i in range(len(ss)):
        print("i: ",i)
        print("path: ",path)
        perm(ss[:i]+ss[i+1:],res,path+ss[i])
        print("%d: " % i)
        print(res)


if __name__ =="__main__":
    string = 'abc'
    print(Permutation(string))