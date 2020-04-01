
# 万物皆对象，python中的类，函数都说对象
# 类名()会做两件事：自动分配内存空间；自动调用初始化方法
# 1.__init__,__del__,__str__

class Dog():
    role = 'Dog'
    def __init__(self):
        print("hello world")

    def print_dog(self):
        print("hello dog")

    def __del__(self):
        print("wo zou le ")

    def __str__(self):
      # 必须返回一个字符串,直接输出对象返回的字符串

        return "我是狗"


print(Dog.role) # Dog
# print(Dog.print_dog()) 报错
dog = Dog() #python类名（）会自动调用init方法
print(dog)
# 如果想提前清理对象，可以使用del
del dog
print("*"*50) #dog是一个全局变量，最后一行代码执行完后才可以销毁。

# 2.身份运算符is,isnot,判断内存地址是否一样（引用的对象），==判断的是两个变量值是否一样
# 判断是否为空时，建议使用is， a is None
a = [1,2,3]
b = [1,2]
print(a is b) #False
print(a == b)#False

b.append(3)
print(a is b)#False
print(a == b)#True

# 3.私有属性和方法
# 属性名和方法名前面增加两个下划线
# python中的属性和方法是伪私有，可以通过_类名__私有对象调用
class Women():
    def __init__(self,weight):
        self.__weight = weight

    def __secret(self):
        print("weight is %d" % (self.__weight))

women = Women(18)
# women.secret()

# 调用私有对象的方法
print(women._Women__weight)
women._Women__secret()