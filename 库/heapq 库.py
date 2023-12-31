# 堆模块。由于堆的数据结构有着 O(logn) 的优秀的算法复杂度，
# 所以在求最值的时候，使用堆往往更加快捷。当然也可以手动实现堆，
# 但Python已经提供了内置堆模块，直接调用即可。
from heapq import *
arr = [2, 5, 1, 3, 9, 8]
heapify(arr)    # 将列表进行堆排列
print(arr[0])   # 输出 1
heappush(arr, 0)    # 数字 0 入堆，自动更新到堆顶
print(arr[0])   # 输出 0
# heapq实现的是小顶堆，也就是堆顶数字保证是最小的。
# 如果要实现大顶堆，使堆顶数字最大，常见的做法是把数字取负再入堆。
