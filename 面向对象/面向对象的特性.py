"""单继承与多继承"""


# 单继承是指一个子类只能继承一个父类的属性和方法。Python中的类可以通过继承来扩展父类的功能，并添加自己的属性和方法。
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


dog = Dog("Tom", "Husky")
dog.eat()  # 输出"Tom is eating."
dog.bark()  # 输出"Tom is barking."


# 这段代码定义了一个Animal类和一个继承自Animal类的Dog类。Animal类有一个构造函数__init__()和一个eat()方法，eat()方法输出动物正在吃东西的信息。
# Dog类有一个构造函数__init__()和一个bark()方法，bark()方法输出狗正在叫的信息。
# 在Dog类的构造函数中，使用super()函数调用父类的构造函数，并传递name参数。然后，为Dog类添加一个名为breed的属性。


# 多继承是指一个类可以同时继承多个父类的特性和方法。
# 多继承的语法非常简单，只需要在定义类时在类名后面添加括号，括号中写上要继承的所有父类的名称，用逗号隔开即可。
class A:
    @staticmethod
    def method1():
        print("Method 1 of A called.")


class B:
    @staticmethod
    def method2():
        print("Method 2 of B called.")


class MyClass(A, B):
    @staticmethod
    def method3():
        print("Method 3 of MyClass called.")


my_object = MyClass()
my_object.method1()  # 输出"Method 1 of A called."
my_object.method2()  # 输出"Method 2 of B called."
my_object.method3()  # 输出"Method 3 of MyClass called."


# 在这个例子中，我们定义了两个父类A和B，它们分别有一个方法method1和method2。然后，我们定义了一个名为MyClass的类，
# 它同时继承了A和B两个父类，并添加了一个方法method3。


# 多层继承:一个类可以同时继承多个父类，这被称为多重继承。多重继承可以形成多层继承，即一个类继承了另一个类，而另一个类又继承了另一个类，以此类推。
class A:
    @staticmethod
    def method1():
        print("Method 1 of A called.")


class B:
    @staticmethod
    def method2():
        print("Method 2 of B called.")


class C(A, B):
    @staticmethod
    def method3():
        print("Method 3 of C called.")


my_object = C()
my_object.method1()  # 输出"Method 1 of A called."
my_object.method2()  # 输出"Method 2 of B called."
my_object.method3()  # 输出"Method 3 of C called."
# 在这个例子中，A类有一个名为method1()的方法，B类有一个名为method2()的方法，C类同时继承了A和B类，并添加了一个名为method3()的方法。
# 在主程序中，我们创建了一个名为my_object的C对象，并调用了它的三个方法，它们分别输出了不同的信息。


"""
Python封装是一种面向对象编程的概念，它指的是将数据和方法封装在一个类中，并且对外部隐藏其实现细节，只暴露必要的接口供外部访问。
封装的目的是为了保护数据的完整性和安全性，防止外部程序意外修改或破坏数据，同时也提高了代码的可维护性和可读性。
"""
# Python中的封装可以通过以下方式实现：
# 1.使用私有变量和方法：在变量或方法名称前加上双下划线“__”即可将其定义为私有的，外部程序无法直接访问。
# 需要注意的是，Python中的私有变量和方法并非完全无法访问，而是通过一定的方式进行访问。
# 2.使用属性：Python中的属性是一种特殊的方法，可以用来控制对类的成员变量的访问。通过属性，可以在访问成员变量时进行一些逻辑判断和处理，
# 从而保护数据的完整性和安全性。
# 3.使用访问器和修改器：访问器和修改器分别是用来获取和设置私有变量的方法，可以在方法内部进行一些逻辑判断和处理，从而保护数据的完整性和安全性。
# 4.使用装饰器：装饰器是Python中一种特殊的语法结构，可以用来修改或扩展函数或类的功能。通过装饰器，可以在类或方法定义时对其进行修饰，
# 从而实现封装的目的。

"""
Python多态是一种面向对象编程的概念，它指的是同一种行为或方法可以在不同的对象上产生不同的结果。换句话说，多态允许不同的对象对同一方法做出不同的响应。
这种特性可以提高代码的灵活性和可扩展性，使程序更加易于维护和扩展。
"""


# 在Python中，实现多态的方式主要有两种：
# 1.方法重写：方法重写是指在子类中重新定义父类的方法，从而实现对该方法的重载。这种方式可以让子类对父类的方法进行扩展或修改，从而实现多态。
# 2.方法重载：方法重载是指在同一类中定义多个同名的方法，但是它们的参数列表不同。这种方式可以让同一个方法名实现不同的功能，从而实现多态。

# 栗子：
# 假设有一个动物类Animal，其中定义了一个speak()方法，不同的动物可以根据自己的特点进行不同的叫声。
# 我们可以定义一个Dog类和一个Cat类继承自Animal类，并且重写speak()方法，使得它们能够发出不同的叫声
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪！")


class Cat(Animal):
    def speak(self):
        print("喵喵喵！")
