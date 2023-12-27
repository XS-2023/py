"""
调用对象，__call__方法的使用
"""


class Demo:
    def __call__(self):
        print('我是 Demo')


demo = Demo()
demo()  # 直接调用对象，实质是调用了他的__call__()


"""
类装饰器的使用案例
"""


class MyLogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("日志纪录...")
        return self.func(*args, **kwargs)


@MyLogDecorator
def fun2():
    print("使用功能2")


if __name__ == '__main__':
    fun2()
