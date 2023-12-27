# 输入一个整数 123
a_1 = int(input())
print(a_1)

# 输入两个或多个整数 12 24 48
a_2, b_2, c_2 = map(int, input().split())
print(a_2, b_2, c_2)

# 输入一行字符串或单个字符 helloPythonExE 或 A
a_3 = input()
print(a_3)

# 输入多个字符串或多个字符 ab bc cd 或 a b c
a_4, b_4, c_4 = input().split()
print(a_4, b_4, c_4)

# 输入一行整数数组形式 1 2 3 4 5 6 7 8
a_5 = list(map(int, input().split()))
print(a_5)

# 输入一行字符数组或字符串数组形式 ab abd abcd ef efg fgh hijk 或 a b c d e f g h i
a_6 = list(input().split())
print(a_6)

# 输入一行需要以特定字符分割的数组形式 ab-cd-ef-gh-ij-kl-mn
a_7 = list(input().split('-'))
print(a_7)

# 列表生成式方式存入一行数组形式输入 aaa bbb ccc 111 123 456 sss
a_8 = [x for x in input().split(' ')]
print(a_8)

# 输入指定行数的字符串或字符
# aaaaa
# bbb
# cccc
# d
# eeee
for x in range(5):
    in_x = input()
print(in_x)

# 输入指定行数的整数(其实只需在上面的基础上加个int即可)

# 输入指定行数的数组形式(以整数元素为例，字符串或字符只需替换map中的int为str）
# 1 2 3 4 5
# 2 3 4 5 6
# 7 8 9 0 1
# 3 3 3 3 3
# 1 3 5 6 7
for x in range(5):
    in_x = list(map(int, input().split()))
print(in_x)

# 以列表生成式方式输入指定行数字符串或字符
# abcd
# 1234
# xyz
# 12abc
# cccc
in_1 = [input() for x in range(5)]
print(in_1)

# 以列表生成式方式输入指定行数整数
# 12
# 345
# 6789
# 567
# 10
in_1 = [int(input()) for x in range(5)]
print(in_1)

# 以列表生成式方式输入指定行数数组形式(字符串或字符数组形式只需替换map中的int为str）
# 123 456 789 1000
# 12 34 56 78
# 77 888 9999
# 1000 100 10 1
# 6 66 666 6666
in_1 = [list(map(int, input().split())) for x in range(5)]
print(in_1)

# 输入不指定行数，并以特定输入为结尾停止输入(以输入字符串‘0000’结束为例）
# 1111
# 2222
# 3333
# 4444
# 0000
while True:
    in_1 = input()
    if in_1 == '0000':
        break

# 输入不确定的行数，并且不知道何时会停止输入
# aaa
# bbbc
# ddd
# eee
# ............还需输入多少行未知
while True:
    try:
        in_1 = input()
    except:
        break
