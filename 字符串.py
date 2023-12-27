# 基本概念

# replace()实现替换
a = 'abcdefghijklmnopqrstuvwxyz'
print(a)
a = a.replace('c', '高')
print(a)

# 字符串切片slice操作  [起始偏移量start：终止偏移量end：步长step]
'''
三个量为正数的情况如下：
[:] 提取整个字符串                                    “abcdef”[:]          “abcdef”              
[start:] 从start索引开始到结尾                        “abcdef”[2:]         “cdef”
[:end] 从头开始直到end-1                             “abcdef”[:2]         “ab”
[start:end] 从start到end-1                          “abcdef”[2:4]        “cd”
[start:end:step] 从start提取到end-1，步长是step       “abcdef”[1:5:2]       “bd”

三个量为负数的情况如下：
"abcdefghijklmnopqrstuvwxyz"[-3:]        倒数三个                         “xyz”
"abcdefghijklmnopqrstuvwxyz"[-8:-3]      倒数第八个到倒数第三个(包头不包尾)    "stuvw"
"abcdefghijklmnopqrstuvwxyz"[::-1]       步长为负，从右到左反向提取           "zyxwvutsrqponmlkjihgfedcba"
'''

# split()分割和join()合并
b = "to be or not to be"
print(b.split())
print(b.split('be'))

c = ['sxt', 'sxt100', 'sxt200']
print('*'.join(c))

# 测试
import time

time01 = time.time()  # 起始时刻
d = ""
for i in range(1000000):
    d += "sxt"
time02 = time.time()  # 终止时刻
print("运算时间：" + str(time02 - time01))
time03 = time.time()  # 起始时刻
li = []
for i in range(1000000):
    li.append("sxt")
d = "".join(li)
time04 = time.time()  # 终止时刻
print("运算时间：" + str(time04 - time03))

# 字符串常用方法汇总

# <常用查找方法>
'''
a="""我是高等,我在北京宏伟堂科技上班。我的儿子叫高洛奇，他6岁了。
我是一个编程教育的普及者，希望影响6000万学习编程的中国人。
我儿子现在也开始学习编程，希望他18岁的时候可以超过我"""

len(a)                         字符串长度                    96
a.startswith('我是高等')        以指定字符串开头                True
a.endswith('过我')             以指定字符串结尾                True
a.find('高')                  第一次出现指定字符串的位置         2
a.rfind('高')                 最后一次出现指定字符串的位置       29
a.count("编程")               指定字符串出现了几次              3
a.isalnum()                  所有字符全是字母或数字            False
'''

# <去除首尾信息>
'''
strip()         去除字符串首尾指定信息
lstrip()        去除字符串左边指定信息
rstrip()        去除字符串右边指定信息
'''
print("*s*x*t*".strip("*"))
print("*s*x*t*".lstrip("*"))
print("*s*x*t*".rstrip("*"))
print("  s xt  ".strip())

# <大小写转换>
'''
a.capitalize()       产生新的字符串,首字母大写              'Gaoqi love programming, love sxt'
a.title()            产生新的字符串,每个单词都首字母大写      'Gaoqi Love Programming, Love Sxt'
a.upper()            产生新的字符串,所有字符全转成大写       'GAOQI LOVE PROGRAMMING, LOVE SXT'
a.lower()            产生新的字符串,所有字符全转成小写       'gaoqi love programming, love sxt'
a.swapcase()         产生新的,所有字母大小写转换            'GAOQI LOVE PROGRAMMING, LOVE sxt'
'''

# <格式排版>
'''
center()、ljust()、rjust()这三个函数用于对字符串实现排版。
'''
e = "SXT"
print(e.center(10, "*"))
print(e.center(10))
print(e.ljust(10, "*"))

# <特征判断方法>
'''
isalnum()   是否为字母或数字
isalpha()   检测字符串是否只由字母组成(含汉字)
isdigit()   检测字符串是否只由数字组成
isspace()   检测是否为空白符
isupper()   是否为大写字母
islower()   是否为小写字母
'''
print("sxt100".isalnum())
print("sxt鸿安堂".isalpha())
print("234.3".isdigit())
print("23423".isdigit())
print("aB".isupper())
print("A".isupper())
print("\t\n".isspace())

# 字符串的格式化
'''
format()基本用法:
基本语法是通过{}和:来代替以前的%
format()函数可以接受不限个数的参数，位置可以不按顺序。
我们可以通过{索引}/{参数名}，直接映射参数值，实现对字符串的格式化，非常方便。
'''
f = "名字是:{0},年龄是：{1}"
print(f.format("高奇", 18))
print(f.format("高希希", 6))

# 填充与对齐
'''
填充常跟对齐一起使用
^、<、>分别是居中、左对齐、右对齐，后面带宽度
:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
'''
print("{:*>8}".format("245"))
print("我是{0},我喜欢数字{1:*^8}".format("高奇", "666"))

# 数字格式化
'''
3.1415926       {:.2f}       3.14        保留小数点后两位
3.1415926       {:+.2f}      3.14        带符号保留小数点后两位
2.71828         {:.0f}       3           不带小数
5               {:0>2d}      05          数字补零(填充左边,宽度为2)
5               {:x<4d}      5xxx        数字补x (填充右边,宽度为4)
10              {:x<4d}      10xx        数字补x (填充右边,宽度为4)
1000000         {:,}         1,000,000   以逗号分隔的数字格式
0.25            {:.2%}       25.00%      百分比格式
1000000000      {:.2e}       1.00E+09    指数记法
13              {:10d}       13          右对齐(默认,宽度为10)
13              {:<10d}      13          左对齐(宽度为10)
13              {:^10d}      13          中间对齐(宽度为10)
'''
g = "我是{0}，我的存款有{1:.2f}"
print(g.format("高奇", 3888.234342))

# 可变字符串
'''
Python中，字符串属于不可变对象，不支持原地修改，如果需要修改其中的值，只能创建新的字符串对象。
确实需要原地修改字符串，可以使用io.StringIO对象或array模块。
'''
import io

s = "hello, sxt"
sio = io.StringIO(s)  # 可变字符串
print(sio)
v1 = sio.getvalue()
print("v1:", v1)
char7 = sio.seek(7)  # 指针知道索引7这个位置
sio.write("gaoqi")
v2 = sio.getvalue()
print("v2:", v2)

# 类型转换
'''
int(x [,base])          将x转换为一个整数
long(x [,base] )        将x转换为一个长整数
float(x)                将x转换到一个浮点数
complex(real[,imag])    创建一个复数
str(x)                  将对象x转换为字符串
repr(x)                 将对象x转换为表达式字符串
eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象
Complex(A)              将参数转换为复数型
tuple(s)                将序列s转换为一个元组
list(s)                 将序列s转换为一个列表
set(s)                  转换为可变集合
dict(d)                 创建一个字典。d必须是一个序列(key,value)元组
frozenset(s)            转换为不可变集合
chr(x)                  将一个整数转换为一个字符
unichr(x)               将一个整数转换为Unicode字符
ord(x)                  将一个字符转换为它的整数值
hex(x)                  将一个整数转换为一个十六进制字符串
oct(x)                  将一个整数转换为一个八进制字符串
'''
# 类型转换
# 转换为int
print('int()默认情况下为：', int())
print('str字符型转换为int：', int('010'))
print('float浮点型转换为int：', int(234.23))
# 十进制数10，对应的2进制，8进制，10进制，16进制分别是：1010,12,10,0xa
print('int(\'0xa\',16) = ', int('0xa', 16))
print('int(\'10\',10) = ', int('10', 10))
print('int(\'12\',8) = ', int('12', 8))
print('int(\'1010\',2) = ', int('1010', 2))
# 转换为float
print('float()默认情况下为：', float())
print('str字符型转换为float：', float('123.01'))
print('int浮点型转换为float：', float(32))
# 转换为complex
print('创建一个复数(实部+虚部)：', complex(12, 43))
print('创建一个复数(实部+虚部)：', complex(12))
# 转换为str字符串
print('str()默认情况下为：', str())
print('float型转换为str：', str(232.33))
print('int转换为str：', str(32))
lists = ['a', 'b', 'e', 'c', 'd', 'a']
print('列表list转换为str:', ''.join(lists))
# 转换为list
strs = 'hongten'
print('序列strs转换为list:', list(strs))
# 转换为tuple
print('列表list转换为tuple:', tuple(lists))
# 字符和整数之间的转换
print('整数转换为字符chr:', chr(67))
print('字符chr转换为整数:', ord('C'))
print('整数转16进制数:', hex(12))
print('整数转8进制数:', oct(12))
