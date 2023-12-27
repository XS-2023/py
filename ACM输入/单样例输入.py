# 在ACM竞赛中，单样例输入通常是只需一行输入的情况。
# 以下是一个示例Python 3代码，用于对10个整数从小到大排序：
numbers = list(map(int, input().split()))
numbers.sort()
for num in numbers:
    print(num, end=' ')

n, m = map(int, input().split())    # 接收两个整数，以空格隔开
arr = list(map(int, input().split()))   # 接收 n 个整数的数组，以空格隔开

# 此外，还可以使用 sys.stdin.readline() 方法直接将一行数据读入，
# 实测这种方式比 input() 函数接收速度要快。
import sys
s = sys.stdin.readline()

# 最省事的方法还是使用sys.stdin.readlines() 方法。
# 和上面说到的 readline() 方法类似，只不过是一次性将所有输入读入，
# 然后转化成一个字符串的列表，再进行后续计算。
import sys
p = sys.stdin.readlines()
# 要注意的是，readlines() 获取到的字符串列表通常会包含一个换行符“\n”，
# 在进行处理的时候，根据需要使用 strip() 或 rstrip() 将最右边的换行符去掉。


n, m = map(int, input().split())        # 输入n、m
a = [int(n) for n in input().split()]   # 输入n个数
a.sort()                                # 排序
for i in range(n-1, n-m, -1):           # 打印出前m-1大的数
    print(a[i], end=' ')
print(a[n-m])                           # 打印出第m大的数

























