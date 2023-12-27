# 序列：列表、元组、字典、集合、字符串

# 列表：用于存储任意数目、任意类型的数据集合。
"""
list.append(x)          增加元素            将元素x增加到列表list尾部
list.extend(aList)      增加元素            将列表alist所有元素加到列表list尾部
list.insert(index,x)    增加元素            在列表list指定位置index处插入元素x
list.remove(x)          删除元素            在列表list中删除首次出现的指定元素x
list.pop([index])       删除元素            删除并返回列表list指定为止index处的元素，默认是最后一个元素
list.clear()            删除所有元素         删除列表所有元素，并不是删除列表对象
list.index(x)           访问元素            返回第一个x的索引位置，若不存在x元素抛出异常
list.count(x)           计数               返回指定元素x在列表list中出现的次数
len(list)               列表长度            返回列表中包含元素的个数
list.reverse()          翻转列表            所有元素原地翻转
list.sort()             排序               所有元素原地排序
list.copy()             浅拷贝             返回列表对象的浅拷贝
"""

# 列表的创建

# 基本语法[]创建
a = [10, 20, 'gaoqi', 'sxt']
print(a)

# list()创建
b = list(range(10))
print(b)

# range()创建整数列表     range([start,]end [,step])
# start参数：可选，表示起始数字。默认是0
# end参数：必选，表示结尾数字。
# step参数：可选，表示步长，默认为1
c = list(range(3, -4, -1))
print(c)

# 推导式生成列表
d = [x * 2 for x in range(100) if x % 9 == 0]
print(d)

# append()方法: 原地修改列表对象，使真正的列表尾部添加新的元素，速度最快，推荐使用。
e = [20, 40]
e.append(80)
print(e)

# +运算符操作: 并不是真正的尾部添加元素，而是创建新的列表对象

# extend()方法: 将目标列表的所有元素添加到本列表的尾部，属于原地操作，不创建新的列表对象。
a.extend(e)
print(a)

# insert()插入元素
e.insert(2, 100)
print(e)

# 乘法扩展: 使用乘法扩展列表，生成一个新列表，新列表元素是原列表元素的多次重复。

# del删除: 删除列表指定位置的元素。
del e[2]
print(e)

# pop()方法: pop()删除并返回指定位置元素，如果未指定位置则默认操作列表最后一个元素。
f = [10, 20, 30, 40, 50]
f1 = f.pop(1)
print(f, f1)

# remove()方法: 删除首次出现的指定元素，若不存在该元素抛出异常。

# index()获得指定元素在列表中首次出现的索引。
# 语法是：index(value,[start,[end]])。其中，start和end指定了搜索的范围。
g = [10, 20, 30, 40, 50, 20, 30, 20, 30]
print(g.index(30, 5, 7))

# count()获得指定元素在列表中出现的次数
print(g.count(20))

# len()返回列表长度，即列表中包含元素的个数。

# 修改原列表，不建新列表的排序
h = [20, 10, 30, 40]
h.sort()  # 默认是升序排列
print(h)
h.sort(reverse=True)  # 降序排列
print(h)
import random

random.shuffle(h)  # 打乱顺序
print(h)

# 建新列表的排序
h1 = sorted(h)
print(h1)
h2 = sorted(h, reverse=True)
print(h2)

# reversed()返回迭代器  返回一次
h3 = reversed(h)
print(h3)
print(list(h3))
print(list(h3))

# max、min、sum函数

# 二维列表
a1 = [
    ["高小一", 18, 30000, "北京"],
    ["高小二", 19, 20000, "上海"],
    ["高小三", 20, 10000, "深圳"],
]
for m in range(3):
    for n in range(4):
        print(a1[m][n], end="\t")
    print()  # 打印完一行,换行

# 元组tuple
"""
列表属于可变序列，可以任意修改列表中的元素。
元组属于不可变序列，不能修改元组中的元素。
因此，元组没有增加元素、修改元素、删除元素相关的方法。
因此，我们只需学元组的创建和删除，元素的访问和计数即可。
"""
# 通过()创建元组，小括号可以省略。
# 如果元组只有一个元素，则必须后面加逗号。
# 这是因为解释器会把(1)解释为整数1，(1,)解释为元组。
# a=(10,20,30)或者a=10,20,30

# 通过tuple()创建元组     tuple(可迭代的对象)
"""
a = tuple()     # 创建一个空元组对象
b = tuple("abc")
c = tuple(range(3))
d = tuple([2,3,4])
"""

# 元组的元素访问、index()、count()、切片等操作，和列表一样。

# 列表关于排序的方法list.sorted()是修改原列表对象，元组没有该方法。
# 如果要对元组排序，只能使用内置函数sorted(tupleObj)，并生成新的列表对象。
a2 = sorted((20, 10, 30, 9, 8))
print(a2)

# zip(列表1，列表2，...)将多个列表对应位置的元素组合成为元组，并返回这个zip对象。
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80, 90, 100]
d = zip(a, b, c)
print(d)  # zip object
e = list(d)  # 列表：[(10, 40, 70), (20, 50,80),(30, 60, 90)]
print(e)

# 使用生成器对象的__next__()方法进行遍历，或者直接作为迭代器对象来使用。
# 不管什么方式使用，元素访问结束后，如果需要重新访问其中的元素，必须重新创建该生成器对象。
s2 = (x for x in range(3))
print(s2.__next__())  # 0
print(s2.__next__())  # 1
print(s2.__next__())  # 2
# print(s2.__next__())        # 报错：StopIteration

# 字典    a = {'name':'gaoqi','age':18,'job':'programmer'}

# 通过{}、dict()来创建字典对象。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
b = dict(name='gaoqi', age=18, job='programmer')
a3 = dict([("name", "gaoqi"), ("age", 18)])
c = {}  # 空的字典对象
d = dict()  # 空的字典对象
print(a)
print(b)
print(a3)
print(c)

# 通过zip()创建字典对象
k = ['name', 'age', 'job']
v = ['gaoqi', 18, 'teacher']
d = dict(zip(k, v))
print(d)  # {'name':'gaoqi','age':18,'job':'techer'}

# 通过fromkeys创建值为空的字典
f = dict.fromkeys(['name', 'age', 'job'])
print(f)
# 结果：{'name':None, 'age':None, 'job':None}

# 通过get()方法获得“值”。❤️推荐使用。
# 优点是：指定键不存在，返回None；也可以设定指定键不存在时默认返回的对象。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
b = a.get('name')
c = a.get('gender', '不存在')
print(b)
print(c)

# 列出所有的键值对
b = a.items()
print(b)

# 列出所有的键，列出所有的值
k = a.keys()
v = a.values()
print(k)
print(v)

# 使用update()将新字典中所有键值对全部添加到旧字典对象上。
# 如果key有重复，则直接覆盖
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
b = {'name': 'gaoxixi', 'money': 1000, 'gender': '男的'}
a.update(b)
print(a)

# 字典中元素的删除，可以使用del()方法；
# 或者clear()删除所有键值对；
# pop()删除指定键值对，并返回对应的“值对象"
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
del (a['name'])
print(a)  # {'age':18, 'job':'programmer'}
age = a.pop('age')
print(age)  # 18

# popitem()：随机删除和返回该键值对。
a = {'name': 'gaoqi', 'age': 18, 'job': 'programmer'}
r1 = a.popitem()
r2 = a.popitem()
r3 = a.popitem()
print(a)  # {}

# 序列解包用于字典时，默认是对“键”进行操作；
# 如果需要对键值对操作，则需要使用items()；
# 如果需要对“值”进行操作，则需要使用values()
s = {'name': 'gaoqi', 'age': 18, 'job': 'teacher'}
name, age, job = s  # 默认对键进行操作
print(name)  # name
name, age, job = s.items()  # 对键值对进行操作
print(name)  # ('name','gaoqi')
name, age, job = s.values()  # 对值进行操作
print(name)  # gaoqi

# 集合: 集合是无序可变，元素不能重复。
# 使用{}创建集合对象，并使用add()方法添加元素
a = {3, 5, 7}
a.add(9)  # {9, 3, 5, 7}

# 使用set()，将列表、元组等可迭代对象转成集合。
# 如果原来数据存在重复数据，则只保留一个
a = ['a', 'b', 'c', 'b']
b = set(a)  # {'b','a','c'}

# remove()删除指定元素；clear()清空整个集合
a = {10, 20, 30, 40, 50}
a.remove(20)  # {10, 50, 40,30}

a = {1, 3, 'sxt'}
b = {'he', 'it', 'sxt'}
print(a | b)  # 并集
print(a & b)  # 交集
print(a - b)  # 差集
print(a ^ b)  # 对称差集
