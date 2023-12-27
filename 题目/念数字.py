"""
题目描述：
输入一个整数，输出每个数字对应的拼音。当整数为负数时，先输出fu字。十个数字对应的拼音如下：

0: ling
1: yi
2: er
3: san
4: si
5: wu
6: liu
7: qi
8: ba
9: jiu
输入格式：
输入在一行中给出一个整数，如：1234。

提示：整数包括负数、零和正数。

输出格式：
在一行中输出这个整数对应的拼音，每个数字的拼音之间用空格分开，行末没有最后的空格。如
yi er san si。

输入样例：
-600
输出样例：
fu liu ling ling
"""
dic = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi',
       '8': 'ba', '9': 'jiu'}
N = input()
for i in range(len(N) - 1):
    if i == 0 and N[i] == '-':
        print('fu', end=' ')
    else:
        print(dic[N[i]], end=' ')
print(dic[N[-1]])
