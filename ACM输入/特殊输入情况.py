# 多行多值输入
# 例如一行中包含多个整数或字符串，每行代表不同的数据。以下是一个示例，计算每行整数的和：
while True:
    try:
        line = input().strip()
        if not line:
            break
        values = list(map(int, line.split()))
        total = sum(values)
        print(total)
    except EOFError:
        raise

# 字符串输入和处理
# 以下是一个示例，统计字符串中的单词数：
while True:
    try:
        line = input().strip()
        if not line:
            break
        words = line.split()
        word_count = len(words)
        print(word_count)
    except EOFError:
        raise

# 大量输入数据的优化
# 以下是一个示例，处理大量整数求和：
total = 0
while True:
    try:
        line = input().strip()
        if not line:
            break
        value = int(line)
        total += value
    except EOFError:
        raise

print(total)
