# python
## 源码
python除了一些函数使用c写在解释器里，一般时候看不到代码，大部分是有python源码的，给开发带来很大的方便。

如何阅读cpython源码？
内置函数用c写的，就需要看源码才能看到逻辑，modules文件夹下。

修改了python源码，不仅c、python写的函数可以改源码，甚至连语法都可以改，可以改grammar中的正则表达式。编译之后生效。

如果在不更改源代码的情况下运行相同的 Python 应用程序两次，第二次总是会快得多。原因就是第二次的时候直接加载了.pyc 字节码然后运行了程序，不像第一次还需要编译生成字节码。

## 内存管理、垃圾回收

垃圾回收以引用计数为主。

导致引用计数+1的情况
+ 对象被创建，例如a=23
+ 对象被引用，例如b=a
+ 对象被作为参数，传入到一个函数中，例如func(a)
+ 对象作为一个元素，存储在容器中，例如list1=[a,a]

导致引用计数-1的情况
+ 对象的别名被显式销毁，例如del a
+ 对象的别名被赋予新的对象，例如a=24
+ 一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
+ 对象所在的容器被销毁，或从容器中删除对象


下载requests
下载库的代码，在test中就有测试代码，有对api的应用和注释很值得一看。

python -v 显示version  
python -m 将库中的python模块用作脚本去运行，使用示例：`python -m SimpleHTTPServer`，一般module中会有`if __name__ == '__main__':`


random
random.seed(10)
如果不主动使用随机数种子，它使用的是当前系统时间。

MISC 杂项 miscellaneous

## MISC

+ 如何生成requirements

生成依赖 pip freeze>requirements.txt
安装所有的依赖 pip install -r requirements.txt 

## python3

函数注解

函数如何写类型声明。Callable
 Callable[[Arg1Type, Arg2Type, ...], ReturnType] 这样的类型注解


 1e-8 10e-7  ！！



 对象 - 类 - 元类是依次抽象的。
+ 对象 - 类 
对象向上抽象一层是类，同一个类下所有对象的相关数据可以类属性的方式存在。比如统计某类创建的实例对象的数量。
```
class Student(object):
    count = 0
    def __init__(self):
        Student.count += 1

student1 = Student()
student2 = Student()
```
+ 类 - 元类
关于类再往上抽象一层即为元类，一个元类下创建的所有的类的相关数据可以交由元类管理。比如记录某元类下所有类的数目。
```
class Meta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if not hasattr(cls, 'registory'):
            # this is the base class
            cls.registory = {}
        else:
            # this is the subclass
            cls.registory[name.lower()] = cls

class Fruit(object):
    __metaclass__=Meta
    pass

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass
```
    
+ 如何理解上述语句？
    + python2和python3使用元类的语法不同。引用元类的方式不同，元类的初始化函数的函数签名也不同
    ```
    # python2 
    class Fruit(object):
        __metaclass__=Meta
        pass
    
    type(name, bases, namespace)
    ```
    
    ```
    # python3 
    class Fruit(object, metaclass=Meta):
        pass
    
    type(name, bases, namespace, **kwargs)
    ```
    + 如何用元类动态创建类？
    可以使用type，动态创建class，动态创建的写法和class的定义写法是等价的，动态创建的class都是新式类，而非经典类。以下两种方式等价：
    ```
    # 使用class语句定义class
    class Base(object):
        counter = 10

    class Derived(Base):
        def get_counter(self):
            return self.counter

    x = Derived()
    print x.get_counter()
    ```

    ```
    # 使用type动态创建class
    Base = type('Base', (), {'counter': 10})
    Derived = type('Derived', (Base,), dict(get_counter=lambda self: self.counter))
    x = Derived()
    print x.get_counter()
    ```
    + 定义类时，元类的哪些成员函数被调用了？ 做下实验：
    ```
    class MyMeta(type):
        def __init__(cls, name, bases, namespace):
            super(MyMeta, cls).__init__(name, bases, namespace)
            print 'type init'

        def __call__(self, *more):
            super(MyMeta, self).__call__(*more)
            print 'call meta'

    class Atest(object):
        __metaclass__ = MyMeta

    class Atestsub(Atest):
        pass

    Atestsub()
    ```
    因为定义了两个类，该文件在import后，会调用MyMeta的init函数两次，在创建类的对象时，会调用一次元类的call函数。对象的类型是对应的class，class的”类型“就是type。class根据元类创建，元类继承于type。所以输出如下
    ```
    type init
    type init
    call meta
    ```
+ 元类的常见用法

用于定义单例
```
class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args)
        return cls.instance

class Test(object):
    __metaclass__=Singleton
```

参考连接：
https://lotabout.me/2018/Understanding-Python-MetaClass
