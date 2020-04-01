
# 单例设计模式：创建的类只有唯一的一个实例，即对象的地址是一样的。
# 使用类名（）创建对象时，首先调用__new__方法分配内存空间，object类提供的内置静态方法。
# 主要作用：1.在内存中为对象分配空间。2.返回对象的引用（self）。
# 如果__new__没有返回对象的引用，就无法进行初始化。

class MusicPlayer():

    def __new__(cls, *args, **kwargs):
        #创建对象时会被自动调用
        print("分配空间")
    #     返回对象的引用
        return super().__new__(cls)

    def __init__(self):
        print("播放器初始化")


mplayer = MusicPlayer()
print(mplayer) #None


# 单例模式，s1与s2的内存地址一样
class Simple():
    # 类属性
    instance = None
    flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if not Simple.flag:
            print("初始化")

        Simple.flag = True

s1 = Simple()
print(Simple.instance)
print(s1)

s2 = Simple()
print(Simple.instance)
print(s2)