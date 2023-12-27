"""
链接：https://ac.nowcoder.com/acm/contest/68712/F
来源：牛客网

题目描述
利用更相减损术求两个整数的最大公约数，即每次将较大的数变成大数减去小数的值
输入描述:
输入两个正整数，范围在1000000以内
输出描述:
输出一个整数
示例1
输入
4 6
输出
2
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b  
    return a


x, y = map(int, input().split())
print(gcd(x, y))
