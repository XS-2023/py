"""
类与对象是面向对象编程中的两个重要概念。
类是一种抽象的数据类型，它定义了一组属性和方法，描述了一类对象的共同特征和行为。
对象是类的实例化，是具体的数据实体，具有类所定义的属性和方法。
对象是类的实例化，是具体的数据实体，具有类所定义的属性和方法。
"""


# Python使用class关键字定义类，使用实例化来创建对象。
class Person:  # 这个类名为Person
    def __init__(self, name, age):  # __init__方法是特殊的方法，它在创建对象时被调用。
        self.name = name  # 它有两个属性name和age
        self.age = age  # self参数是指向对象本身的引用，可以在方法内部使用来访问对象的属性和方法。

    def eat(self):  # 以及三个方法eat、sleep和work
        print(self.name + " is eating.")

    def sleep(self):
        print(self.name + " is sleeping.")

    def work(self):
        print(self.name + " is working.")


# 这个例子创建了一个名为p的Person对象，它的name属性为"Tom"，age属性为20:
p = Person("Tom", 20)

# 可以通过对象的属性和方法来访问和修改对象的状态：
print(p.name)  # 输出"Tom"
p.eat()  # 输出"Tom is eating."
p.name = "Jerry"
p.sleep()  # 输出"Jerry is sleeping."

"""生动举例："""


class WashingMachine:
    h = 850
    w = 460
    c = 595
    brand = '海尔'

    # self 自己 具体的一个对象

    def __init__(self):
        self.__color = 'red'  # 设置属性或者方法为私有方法
        # 在属性或者方法前加两根下划线

    def get_color(self):
        """获取颜色"""
        return self.__color

    def set_color(self, color):
        """设置颜色"""
        if color in ['red', 'blue', 'yellow']:
            self.__color = color
        else:
            print('违规的颜色')

    @staticmethod
    def start():
        print('启动洗衣机，开始洗衣服')

    @staticmethod
    def stop():
        print('关闭洗衣机')


# 类通过加括号来进行使用 生成一个具体的对象
haier1 = WashingMachine()
haier1.set_color('blue')  # 通过给予的修改方法，去修改对象里面的颜色
print(haier1.get_color())  # 通过get方法获取当前的颜色

"""
在Python中，一个类可以从另一个类继承，被继承的类称为父类， 继承的类称为子类。
子类可以继承父类的属性和方法，并且可以添加自己的属性和方法。
子类也可以重写父类的方法，从而改变其行为。
"""


# 例如，下面的代码创建了一个Animal类作为父类，然后创建了一个Dog类作为子类：
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "Woof"


my_dog = Dog("Rufus")
print(my_dog.name)
print(my_dog.speak())
# 在这个例子中，Animal类包含一个构造函数和一个抽象方法speak。Dog类继承了Animal类，并重写了speak方法。
# 我们可以创建一个Dog对象并调用它的方法，它将返回“Woof”。
