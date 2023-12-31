"""
链接：https://ac.nowcoder.com/acm/contest/68712/H
来源：牛客网

题目描述
在一个排列中，如果一对数的前后位置与大小顺序相反，即前面的数大于后面的数，那么它们就称为一个逆序。一个排列中逆序的总数就称为这个排列的逆序数。
比如一个元素个数为4的数列，其元素为2，4，3，1，则(2,1)，(4,3)，(4,1)，(3,1)是逆序，逆序数是4
现在求给定数列的逆序数
输入描述:
第一行为N，表示数列的元素个数(N<=2000)
第二行为N个用空格隔开的整数,其值在int范围内
输出描述:
输出占一行，为逆序数的个数
示例1
输入
4
2 4 3 1
输出
4
"""
N = int(input())
s = 0

c = list(map(int, input().split()))

for i in range(N - 1):
    for j in range(i + 1, N):
        if c[i] > c[j]:
            s += 1

print(s)
