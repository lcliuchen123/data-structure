
# 同城艺龙笔试放弃
# sql: row_number() over(order by ) 1，2，3，4，5，6
# sql: rank() over (order by) 1,2,3,3,4,5
#万物皆对象， 类，函数本身就是一个实例化的对象

class Dog():
    role = 'Dog'

    def print_dog(self):
        print("hello")


print(Dog.role) #Dog ？？？？？？？？
# print(Dog.print_dog()) #报错
dog1 = Dog()
print(dog1)
dog2 = Dog()
print(dog2)