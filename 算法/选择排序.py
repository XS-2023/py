# 选择排序是一种不稳定的排序算法，它每次选择未排序部分的最小元素并将其放在已排序部分的末尾。
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
