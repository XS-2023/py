# 0/1背包问题要求在限定重量的情况下，选择物品以获得最大价值。
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# 分数背包问题允许部分取物品，目标是最大化总价值。
def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    items = list(zip(weights, values, [v / w for v, w in zip(values, weights)]))
    items.sort(key=lambda x: x[2], reverse=True)
    max_value = 0
    for w, v, ratio in items:
        if capacity >= w:
            max_value += v
            capacity -= w
        else:
            max_value += ratio * capacity
            break
    return max_value
