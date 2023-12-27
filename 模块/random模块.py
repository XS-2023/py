import random

rand_int = random.randint(1, 10)  # 生成1到10之间的随机整数
rand_float = random.uniform(0, 1)  # 生成0到1之间的随机浮点数

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  # 随机打乱列表元素的顺序

random.seed(42)  # 设置随机种子为42
rand_num = random.randint(1, 10)  # 随机数是确定的
