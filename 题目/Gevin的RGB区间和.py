"""
链接：https://ac.nowcoder.com/acm/contest/70472/I
来源：牛客网

题目描述
给你一个n∗n（2 ≤ n ≤ 1000，且 n 必定为偶数）大小的二维数组，二维数组上有三块不同颜色的区间
请你求出三个区间内的元素和。
(颜色在边缘的长度一个是 n/2)
R R G G
R G G G
G G G B
G G B B
输入描述:
输入一个 n 表示二维数组的大小（2 ≤ n ≤ 10^3，且 n 必定为偶数）
下面 n 行输入 n 个整数a[i][j]（1 ≤ a[i][j] ≤ 10^3）
输出描述:
分别输出三个区间的元素和
示例1
输入
4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
输出
3 10 3
"""
n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]
sum1, sum2, sum3, sum_ = 0, 0, 0, 0
for i in range(n // 2):
    for j in range(n // 2 - i):
        sum1 += a[i][j]
for i in range(n // 2):
    for j in range(n // 2 - i):
        sum3 += a[n - i - 1][n - j - 1]
for i in range(n):
    for j in range(n):
        sum_ += a[i][j]
sum2 = sum_ - sum1 - sum3
print(sum1, sum2, sum3)
