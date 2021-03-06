# 前言

在编程时，经常需要检查一系列的条件，并据此决定采取什么样的措施，在Python中，if语句能够让你检查程序的当前状态，并采取相应的措施。

在本篇文章中，我将教你学会条件测试，以检查所关心的任何条件。你将学习简单的if语句，以及创建一系列复杂的fi语句来确定当前到底处于什么情形。

那么接下来，我们便可以将学习到的知识应用在列表当中，使用你想要的方式去处理列表中的元素。

# 简单案例

下面是一个简短的案例，演示了如何使用if语句来正确处理特殊的情形。假设你有一个汽车列表，并想将其中的汽车名称打印出来。对于大多数汽车，应该首字母大写的方式打印其名称，但对于汽车'bmw'，应该全大写的方式打印。下面的代码遍历这个列表，并以首字母大写的方式打印整个汽车列表。

具体代码，如下所示：

```python
cars = ['audi', 'bwm', 'subaru', 'toyota']

for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())
```

## 条件测试

每条if语句都是一个值为True或False的表达式，这种表达式称为条件测试。Python根据条件测试的值为True还是False来判断是否执行if语句中的代码，如果条件测试为True，那么Python就执行紧跟在if语句后面的代码；如果为False，Python就会忽略if语句的代码。

## 检查是否相等

大多数条件测试将一个变量的当前值同特定的值进行比较。最简单的条件测试检查变量的值是否与特定值相等。

例如：

```python
car = 'bwm'
print(car == 'bwm')
```

一个等号，其实是把变量car的值设置为'bwm'，两个等号则是相当于发问：car的值和'bwm'相等吗？

## 检查是否相等时忽略大小写

在Python中检查是否相等时区分大小写。例如两个大小写不同的值视为不相等。

```python
>>> car = 'Audi'
>>> car == 'audi'
False
```

如果大小写很重要，这种行为有其优点。但是如果大小写无关紧要，只想检查变量的值，可以将变量的值转换为小写。再进行比较：

```python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
```

这个方法可以用于网站的注册，网站可以使用这个方式来确保用户是独一无二的，而并非是与另一个用户名的大小写不相同。用户提交新的用户名时，将它转换为小写，并与所有既有的小写用户名版本进行比较。执行这种检查时，如果已经有了用户名'john'，则用户提交用户名'john'时将会遭到拒绝。

