"""
python重写
在Python中，子类可以重写（覆盖）父类的方法，以实现自己的功能。
重写方法时，需要注意以下几点：
1.子类的方法名与父类的方法名相同。
2.子类的方法参数与父类的方法参数相同。
3.子类的方法返回值类型与父类的方法返回值类型相同或者是父类方法返回值类型的子类型。
"""


class Animal:
    @staticmethod
    def make_sound():
        print("The animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")


my_dog = Dog()
my_dog.make_sound()  # 输出"The dog barks."

# 在这个例子中，Animal类有一个名为make_sound()的方法，它输出“动物发出声音”的信息。Dog类继承了Animal类，并重写了make_sound()方法，
# 使其输出“狗叫”的信息。在主程序中，我们创建了一个Dog对象my_dog，并调用了它的make_sound()方法，输出了“狗叫”的信息。

"""
python调用
在Python中，调用父类的方法有两种方式：
1.使用super()函数调用父类的方法。
2.直接使用父类的类名调用父类的方法。
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(self.name + " is barking.")


my_dog = Dog("Tom", "Husky")
my_dog.eat()  # 输出"Tom is eating."


# 在这个例子中，Animal类有一个名为eat()的方法，它输出动物正在吃东西的信息。Dog类继承了Animal类，
# 并使用super()函数调用了父类的构造函数__init__()，以初始化name属性。在主程序中，我们创建了一个名为my_dog的Dog对象，
# 并调用了它的eat()方法，输出了“Tom is eating.”的信息。

# 直接使用父类的类名调用父类的方法也是一种有效的方式:

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating.")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(self.name + " is barking.")


my_dog = Dog("Tom", "Husky")
my_dog.eat()  # 输出"Tom is eating."

# 在这个例子中，Dog类的构造函数使用Animal类名和self参数调用了父类的构造函数__init__()，以初始化name属性。
# 在主程序中，我们创建了一个名为my_dog的Dog对象，并调用了它的eat()方法，输出了“Tom is eating.”的信息。

"""
super函数
在Python中，super()函数用于调用父类的方法。使用super()函数调用父类的方法时，可以不使用父类的类名，而使用super()函数自动识别出需要调用的父类的方法。
super()函数的语法： super([type[, object-or-type]])
其中，type是子类的类型，object-or-type是子类的对象或类型。如果只有一个参数，则默认为子类的类型。
"""


# 下面的代码定义了一个名为Animal的父类和一个名为Dog的子类，子类使用super()函数调用了父类的方法：
class Animal:
    def __init__(self, nam0e):
        self.name = name

    def eat(self):
        print(self.name + " is eating.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(self.name + " is barking.")


my_dog = Dog("Tom", "Husky")
my_dog.eat()  # 输出"Tom is eating."
