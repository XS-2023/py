"""
这是一条检测真正程序员的段子：假如你被家人要求下班顺路买十只包子，如果看到卖西瓜的，买一只。那么你会在什么情况下只买一只包子回家？
本题要求你考虑这个段子的通用版：假如你被要求下班顺路买 N 只包子，如果看到卖 X 的，买 M 只。那么如果你最后买了 K 只包子回家，说明你看到卖 X 的没有呢？

输入格式：
输入在一行中顺序给出题面中的 N、X、M、K，以空格分隔。其中 N、M 和 K 为不超过 1000 的正整数，X 是一个长度不超过 10 的、仅由小写英文字母组成的字符串。题目保证 N

=M。

输出格式：
在一行中输出结论，格式为：

如果 K=N，输出 mei you mai X de；
如果 K=M，输出 kan dao le mai X de；
否则输出 wang le zhao mai X de.
其中 X 是输入中给定的字符串 X。
输入样例 1：
10 xigua 1 10
输出样例 1：
mei you mai xigua de
输入样例 2：
10 huanggua 1 1
输出样例 2：
kan dao le mai huanggua de
输入样例 3：
10 shagua 1 250
输出样例 3：
wang le zhao mai shagua de
"""


def solve(N, X, M, K):
    if K == N:
        print("mei you mai {0} de".format(X))
    elif K == M:
        print("kan dao le mai {0} de".format(X))
    else:
        print("wang le zhao mai {0} de".format(X))


N, X, M, K = input().split()
N, M, K = int(N), int(M), int(K)
solve(N, X, M, K)
