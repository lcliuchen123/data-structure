
# 第一题 AC20,可能有重复
n = int(input())
data = []
for i in range(n):
    line = input()
    line = line.split()
    data.append(line)

data.sort()
d= {}
name = set([])
for item0 in data:
    for item1 in data:
        if item0 == item1:
            continue
        key = (item0[0],item1[0])
        if item0[1] == item1[1]:
            if item0[1] not in name:
                name.add(item0[1])
                d[key] = d.get(key,0) + 1

keys = list(d.keys())
keys.sort()
for k in keys:
    if d[k] > 2:
        print("%s %s %d" %(k[0],k[1],d[k]))


#第二题?????????????????????
# 作者：哎我说命运啊
# 链接：https://www.nowcoder.com/discuss/251447?type=post&order=time&pos=&page=1
# 来源：牛客网

import copy
import sys

def helper(dp,t):
    result = 1
    tp = {}
    for i in t:
        if i in tp:
            tp[i] = tp[i]+1
        else:
            tp[i] = 1
    for i in tp:
        result = result*dp[tp[i]]
    value = 1
    for i in t:
        value = value*dp[i+1]
    rp = dp[len(t)]/result
    return rp,value

def dfs(dp,n,temp,res,k,m):
    if len(temp)>m:
        return
    if n == sum(temp):
        l = len(temp)
        rp,value = helper(dp,temp)
        res.append([l,rp,value])
        return
    if n < sum(temp):
        return
    for i in range(k,n+1):
        temp.append(i)
        dfs(dp,n,copy.deepcopy(temp),res,i,m)
        temp = temp[:-1]

def f(n,m):
    if m==1:
        print(1)
        return
    r = 0
    dp = {1:1}
    for i in range(2,n+1):
        dp[i] = i*dp[i-1]
    Ann = dp[n]
    res = []
    temp =[]
    dfs(dp,n-m,temp,res,1,m)
    for i in res:
        l,rp,value = i
        if m==l:
            cmn=1
        else:
            cmn = dp[m]/dp[m-l]/dp[l]
        r = cmn*Ann*rp/value + r
    print(int(r))

a = sys.stdin.readline()
a = a.split()
n,m = int(a[0]),int(a[1])
f(n,m)


# 第三题,梯度更新溢出
import numpy as np

def loss_fun(label,theta,train):
    ans = 0
    m = len(label)
    for i in range(m):
        hi = get_pro(theta, train[i])
        ans += label[i] * np.log(hi) + (1-label[i]) * np.log(1-hi)
    ans  = ans / m
    res = lam*np.sum(np.dot(theta,theta)) / m
    ans += res

    return ans

def get_pro(theta,x):
    h = 1/ (1+np.exp(-np.dot(theta,x)))

    return h

def get_dh(train,label,lam,theta):
    ans = 0
    m =len(label)
    for i in range(m):
        # print(i)
        hi = get_pro(theta,train[i])
        print("hi: ", hi)
        dhi = -train[i] * (label[i] - hi)
        # print("dhi: ", dhi)
        # if label[i] == 1:
        #     dhi = label[i] *hi *(-1)*train[i] *np.exp(-np.dot(theta,train[i]))
        # else:
        #     dhi = (1-label[i])*(hi ** 2) /(1-hi) * train[i] *np.exp(-np.dot(theta,train[i]))
        # print("hi: ",hi)
        ans += dhi

    ans = ans / m
    res = lam * np.sum(np.dot(theta,theta))/m
    ans += res

    return ans


line = input()
line = [float(x) for x in line.split()]
alpha,lam,epoch,n,m,l = line
epoch = int(epoch)
n = int(n)
m = int(m)
l = int(l)
train = []
label = []
test = []
for i in range(m+l):
    line = input()
    line = [float(x) for x in line.split()]
    if i <m:
        train.append(line[:-1])
        label.append(line[-1])
    else:
        test.append(line)

train = np.array(train)
label = np.array(label)
test = np.array(test)
theta_0 = np.ones(n)
# print("train: ",train)
# print("label: ", label)
# print("test: ",test)
# print("theta0: ", theta_0)

j =0
while j < epoch:
    print('*******%d*****' % j)
    old_theta = theta_0
    print("old_theta: ", old_theta)
    dh = get_dh(train,label,lam,theta_0)
    print("dh: ", dh)
    theta_0 = old_theta - alpha * dh
    df_theta = theta_0 - old_theta
    print("theta: ", theta_0)
    old = loss_fun(label,old_theta,train)
    new = loss_fun(label,theta_0,train)
    if  np.abs(new-old)<0.00001:
        break
    j += 1

# theta_0 = np.array([ 0.12794378, -0.00556141, -0.01515605,  0.15241489,  0.02586652])
for  k in range(l):
    print("k: ",k)
    hk = get_pro(theta_0,test[k])
    print(hk)
    if hk >0.5:
        print(1)
    else:
        print(0)

# 0.1 10 100 5 10 10
# 0.105 0.956 0.876 0.133 0.249 0
# 0.195 0.672 0.193 0.016 0.009 0
# 0.059 0.282 0.709 0.139 0.478 1
# 0.303 0.39 0.95 0.912 0.522 1
# 0.59 0.57 0.141 0.959 0.036 1
# 0.231 0.355 0.305 0.508 0.625 1
# 0.896 0.415 0.771 0.197 0.826 0
# 0.051 0.537 0.442 0.46 0.628 0
# 0.737 0.583 0.09 0.337 0.774 1
# 0.062 0.217 0.553 0.868 0.87 0
# 0.13 0.972 0.845 0.737 0.492
# 0.016 0.009 0.432 0.41 0.092
# 0.257 0.327 0.451 0.18 0.62
# 0.774 0.143 0.879 0.123 0.222
# 0.885 0.114 0.352 0.484 0.367
# 0.439 0.227 0.675 0.654 0.323
# 0.778 0.191 0.633 0.628 0.929
# 0.958 0.231 0.07 0.739 0.34
# 0.015 0.115 0.154 0.75 0.649
# 0.283 0.853 0.752 0.915 0.937
# 0
# 1
# 0
# 0
# 1
# 1
# 1
# 1
# 1
# 1