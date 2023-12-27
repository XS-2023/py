# coding=utf-8
from functools import wraps


def mylog(func):
    @wraps(func)
    def infunc(*args, **kwargs):
        print("日志纪录...")
        print("函数文档:", func.__doc__)
        return func(*args, **kwargs)

    return infunc


@mylog  # fun2 = mylog(fun2)
def fun2():
    """强大的功能2"""
    print("使用功能2")


if __name__ == '__main__':
    fun2()
    print("函数文档--->", fun2.__doc__)

"""
运算结果：
日志纪录...
函数文档: 强大的功能2
使用功能2
函数文档---> 强大的功能2
"""
