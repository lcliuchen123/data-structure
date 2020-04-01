
# 1.实例
try:
    num = int(input("输入一个整数： "))
    num = 8 / num
except ValueError:
    print("请输入正确的整数")

except ZeroDivisionError:
    print("!=0")

# 捕获未知错误
except Exception as result:
    print("未知错误： %s" % result)

print('*'*50)

# 2.捕获异常的完整语法
try:
    pass
except ValueError:
    pass

except Exception as result:
    print(result)

# 没有异常时才会执行else下方的代码
else:
    pass
# 无论是否异常都会被执行
finally:
    pass

#3.异常的传递，异常传递给函数、方法的调用方
# 利用异常的传递性捕获异常

def demo1():
    return int(input("输入整数： "))

def demo2():
    return demo1()

try:
   print(demo1())
   print(demo2())
except Exception as result:
    print(result)

# 主动抛出异常

def input_password():
    password = input("输入密码： ")
    if len(password) >= 8:
        return password
    else:
        print("主动抛出异常")
        ex = Exception("密码长度不够")

        raise ex
try:
    print(input_password())
except Exception as result:
    print(result)