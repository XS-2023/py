# 多样例输入，无明确样例个数
# 以下是一个示例，计算每组输入的和：
while True:
    try:
        data = list(map(int, input().strip().split()))
        num_inputs, values = data[0], data[1:]
        total = sum(values)
        print(total)
    except EOFError:
        raise

# 要输入N行
# 以下是一个示例，计算每组输入的和：
num_cases = int(input().strip())
for case in range(num_cases):
    data = list(map(int, input().strip().split()))
    num_inputs, values = data[0], data[1:]
    total = sum(values)
    print(total)
