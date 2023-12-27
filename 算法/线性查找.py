# 线性查找遍历列表以查找特定元素。
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
