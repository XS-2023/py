# Counter类
# 将对象按照其中元素的出现次数，自动转化为一个类似字典的计数类。与字典大同小异，但是可以进行计算。
from collections import Counter
a = "aaabbbccc"
b = "abcdef"
result = Counter(a) - Counter(b)
print(result)     # Counter({'a': 2, 'b': 2, 'c': 2})

# deque类
# 双端列表，使用方法和普通列表类似，不同的是其可以在列表两端以 O(1) 的复杂度入队、出队，在单调队列、广度搜索 BFS 等题目中使用较多。
# 比如下面这个求滑动窗口最小值的单调队列模板题：
from collections import deque
q = deque()   # 队列中保存的是数组的下标
for i in range(n):
    while q and arr[q[-1]] > arr[i]: q.pop()     # 如果新的数字比队尾数字小，则队尾数字出队
    q.append(i)     # 新的数字入列
    if i >= k - 1:     # 当窗口滑动到k时才开始输出
        while q and q[0] <= i - k: q.popleft()     # 如果队首划出窗口，则队首数字出队
        print(arr[q[0]], end=" ")      # 打印队首
        