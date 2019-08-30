
# 1.单继承
# 继承的传递性，Aimal->Dog->XiaoTian
# 子类不能调用父类的私有属性和方法

class Animal():
    def eat(self):
        print("animal eat")

    def drink(self):
        print("animal drink")

    def sleep(self):
        print("animal sleep")


class Dog(Animal):
    def drink(self):
        print("dog drink")

    def bar(self):
        print("dog bar")

class XiaoTian(Dog):
    def fly(self):
        print("fly")

#         调用父类
        super().bar()
        Dog.bar(self)

# animal = Animal()
# animal.drink()
# dog = Dog()
# dog.drink()   #当父类与子类有相同的函数时，调用子类的
# xiao = XiaoTian()
# xiao.drink()
# xiao.bar()
# xiao.fly()

animal = Animal()
animal.drink()# animal drink
print(animal)
animal = Dog()
animal.drink()#dog drink
print(animal)

# 2.多继承
# 父类A,B如果有相同的方法，按照继承顺序调用
class  A():
    def test(self):
        print("a")

class B():
    def test(self):
        print("b")

class C(A,B):
    def test_c(self):
        print("c")

c = C()
c.test() #按照继承顺序调用

# 小科普
# 1.方法搜索顺序
print(C.__mro__)

# 2.新式类和旧式类
# 新式类以object为基类，旧式类不以object为基类，但是python3默认以object为基类
print(dir(c)) #查看内置属性和方法

# 多态，不同的子类调用相同的方法