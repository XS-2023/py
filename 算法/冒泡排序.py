# 冒泡排序是一种简单的排序算法，它多次遍历列表，比较相邻元素并交换它们。
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
