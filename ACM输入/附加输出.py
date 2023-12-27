# 四舍五入输出
value = 3.14159265359
rounded_value = round(value, 2)
print(rounded_value)

# 小数精度控制
value = 3.14159265359
formatted_value = "{:.2f}".format(value)
print(formatted_value)

#  输出重定向到文件
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)

# 要求输出数字以空格分开。其实 print() 函数的参数 sep=" " 的默认值就是空格，
# 所以如果最后的答案是一个列表或其他可迭代对象，可以使用星号 * 对其进行解包，
# 然后再利用print() 将其以空格隔开进行输出。
result = [1, 2, 3, 4, 5]
print(*result)
# 关于解包，可以理解为就是把列表左右的括号去掉（保留元素间隔的逗号）。
# 比如上面例子里如果 result = [1, 2, 3, 4, 5]，那么 print(*result)
# 等价于 print(1, 2, 3, 4, 5)，然后 sep 参数会将逗号变成空格再输出。

# 同理，如果要求输出每个数字占一行，则可以在解包列表的同时，
# 将 print() 函数的 sep 参数设置为换行符 “\n”即可。
print(*result, sep="\n")
