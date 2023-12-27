"""
链接：https://ac.nowcoder.com/acm/contest/68712/I
来源：牛客网

题目描述
给你一个整数n, 判断它是否是素数。注意1不是素数。
输入描述:
第一行输入一个整数T,表示需要判断的数的个数

接下来T行每行一个整数n,表示需要判断的数。

1<=n<=1e5,1<=T<=10
输出描述:
输出T行，判断是否是素数。是，输出“Yes”，否则输出“No”
示例1
输入
2
1
2
输出
No
Yes
"""
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())

for _ in range(n):
    a = int(input())
    if is_prime(a):
        print("Yes")
    else:
        print("No")