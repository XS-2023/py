# 多样例输入，无明确样例个数
# 以下是一个示例，对两个整数求和：
while True:
    try:
        a, b = map(int, input().strip().split())
        print(a + b)
    except EOFError:
        break

# 要输入N行
# 以下是一个示例，计算学生的平均成绩和最高分学生的数据：
num_students = int(input().strip())

def is_numeric(x):
    if ord(x[0]) < 90:  # 判断是数字还是字母
        return int(x)
    return x

data = [list(map(is_numeric, input().split())) for i in range(num_students)]

average = sum([x[2] for x in data]) / num_students
print(int(average), end=' ')
max_score_student = max(data, key=lambda x: sum(x[2:]))
print(*max_score_student)


# 多样例输入，指定结束符号
# 以下是一个示例，计算整数对的和，直到遇到输入0 0：
while True:
    a, b = map(int, input().strip().split())
    if a == 0 and b == 0:
        break
    print(a + b)


# 输入N组，指定结束符号
# 以下是一个示例，计算整数对的和，直到遇到输入0 0：
num_cases = int(input().strip())
for case in range(num_cases):
    a, b = map(int, input().strip().split())
    if a == 0 and b == 0:
        break
    print(a + b)
