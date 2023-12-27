"""
property 装饰器用于类中的函数，使得我们可以像访问属性一样来获取一个函数的返回值。
"""


class User:
    def __init__(self, name, month_salary):
        self.name = name
        self.month_salary = month_salary

    @property
    def year_salary(self):
        return int(self.month_salary) * 12


if __name__ == '__main__':
    u1 = User("gaoqi", "30000")
    print(u1.year_salary)


"""
staticmethod 装饰器同样是用于类中的方法，这表示这个方法将会是一个静态方法，
意味着该方法可以直接被调用无需实例化，但同样意味着它没有 self 参数，也无法访问实例化后的对象。
"""


class Person:

    @staticmethod
    def say_hello():
        print("hello world!")


if __name__ == '__main__':
    Person.say_hello()


"""
classmethod 这个方法是一个类方法。该方法无需实例化，没有 self 参数。
相对于 staticmethod 的区别在于它会接收一个指向类本身的 cls 参数。
"""


class Person:

    @classmethod
    def say_hello(cls):
        print(f"我是{cls.__name__}")
        print("hello world!")


if __name__ == '__main__':
    Person.say_hello()
