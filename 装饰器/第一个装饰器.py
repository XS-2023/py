
# 开闭原则
# 第一个装饰器
def mylog(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print("日志记录")
    return inner


@mylog  # fun1 = mylog(fun1)
def fun1():
    print("使用功能1")


@mylog  # fun2 = mylog(fun2)
def fun2(a, b):
    print("使用功能2", a, b)


fun1()
fun2(100, 200)
