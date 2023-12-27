# 偏函数
import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))  # 64
print(int2('1010101'))  # 85
print(int2('1000000', base=10))  # 也可以修改base的值

# 闭包
"""
闭包的特点：
1.存在内外层函数嵌套的情况
2.内层函数引用了外层函数的变量或者参数（自由变量）
3.外层函数把内层函数的这个函数本身当做返回值进行返回
"""


def outer():
    print("outer")
    a = 1

    def inner():
        print("inner")
        nonlocal a  # 闭包是由于函数内部使用了函数外部的变量。
        # 这个函数对象不销毁，则外部函数的局部变量也不会被销毁。
        print(f"a:{a}")

    return inner


inn = outer()
print("-----")
inn()

# coding=utf-8
# 需求：实现变量a 自增
# 通过全局变量，可以实现，但会污染其他程序
a = 10


def add():
    global a
    a += 1
    print("a:", a)


def print_ten():
    if a == 10:
        print("ten!")
    else:
        print("全局变量a，不等于10")


add()
add()
add()
print_ten()
"""
运行效果：
a: 11
a: 12
a: 13
全局变量a，不等于10
"""

# coding=utf-8
# 需求：实现变量a 自增
# 通过局部变量，不能实现递增
a = 10


def add():
    a = 10
    a += 1
    print("a:", a)


def print_ten():
    if a == 10:
        print("ten!")
    else:
        print("全局变量a，不等于10")


add()
add()
add()
print_ten()
"""
运行结果：
a: 11
a: 11
a: 11
ten!
"""

# coding=utf-8
# 需求：实现变量a 自增
# 通过闭包，也没有污染全局变量a。也实现了自增
a = 10


def add():
    a = 10

    def increment():
        nonlocal a
        a += 1
        print("a:", a)

    return increment


def print_ten():
    if a == 10:
        print("ten!")
    else:
        print("全局变量a，不等于10")


increment = add()
increment()
increment()
increment()
print_ten()
print("global a:", a)
"""
运算结果：
a: 11
a: 12
a: 13
ten!
global a:10
"""


# 用闭包实现不修改源码添加功能
# 本次内容，是装饰器的基础

def outfunc(func):
    def infunc(*args, **kwargs):
        print("日志纪录 start...")
        func(*args, **kwargs)
        print("日志纪录 end...")

    return infunc


def fun1():
    print("使用功能1")


def fun2(a, b, c):
    print("使用功能2", a, b, c)


print(id(fun1))
fun1 = outfunc(fun1)
print(id(fun1))
fun1()
fun2 = outfunc(fun2)
fun2(100, 200, 300)

# map函数
"""
map()函数接收两种参数，一是函数，
一种是序列(可以传入多个序列)，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
"""


def f(x):
    return x * x


L = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(L))

L = map(lambda n: n * n, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(L))

L = map(lambda x, y: x + y, [1, 2, 3, 4], [10, 20, 30])
print(list(L))

# reduce函数
"""
reduce位于functools模块
reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
from functools import reduce


def add(x, y):
    return x + y


sum0 = reduce(add, [1, 3, 5, 7, 9])
print(sum0)

# filter函数
"""
内置函数filter()用于过滤序列.
filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False, 决定保留还是丢弃该元素。
"""
# filter过滤列表，删掉偶数，只保留奇数
L = filter(lambda n: n % 2 == 1, [1, 2, 4, 5])
print(list(L))

# filter序列中的空字符串删掉
L = filter(lambda s: (s and s.strip()), ['A', '', 'B', None, 'C', '  '])
print(list(L))

# sorted函数
"""
排序算法，排序也是在程序中经常用到的算法。
无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
1.如果是数字，我们可以直接比较
2.如果是自定义对象呢？直接比较数学上的大小是没有意义的，
因此，比较的过程必须通过函数抽象出来。
通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1，
这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序
"""
# sorted对list进行排序
sorter1 = sorted([1, 3, 6, -20, 34])
print("升序排列:", sorter1)

# sorted()函数也是高阶函数，它还可以接收一个key函数来实现自定义的排序
sorter2 = sorted([1, 3, 6, -20, -70], key=abs)
print("自定义排序:", sorter2)

sorter2 = sorted([1, 3, 6, -20, -70], key=abs, reverse=True)
print("自定义反向排序:", sorter2)

# 4.2 字符串排序依照ASCII
sorter3 = sorted(["ABC", "abc", "D", "d"])
print("字符串排序:", sorter3)

# 4.3 忽略大小写排序
sorter4 = sorted(["ABC", "abc", "D", "d"], key=str.lower)
print("忽略字符串大小写排序:", sorter4)

# 4.4 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
sorter5 = sorted(["ABC", "abc", "D", "d"], key=str.lower, reverse=True)
print("忽略字符串大小写反向排序:", sorter5)

# sorted对自定义对象的排序
from functools import cmp_to_key


class Student:
    def __init__(self, age, name):
        self.name = name
        self.age = age


def custom_sorted(stu1, stu2):
    if stu1.age < stu2.age:
        return -1
    if stu1.age > stu2.age:
        return 1
    return 0


stu1 = Student(41, 'aaa')
stu2 = Student(21, 'ccc')
stu3 = Student(31, 'bbb')
# student_list = sorted([stu1, stu2, stu3], key=lambda x: x.age)
student_list = sorted([stu1, stu2, stu3], key=cmp_to_key(custom_sorted))
for stu in student_list:
    print('name:', stu.name, 'age:', stu.age)
