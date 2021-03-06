> 在学习之前，需要各位小伙伴具有百度的搜索能力。本系列分享的每一章都是核心知识。在编程的过程当中遇到的问题可以自己百度可以解决的一定要自己解决，实在是不会再问问题。

# 前言

在上一次文章中，为大家分享了什么是列表，以及列表的增删改查的四种用法。跟着代码进行学习，相信大家应该可以学到不少的东西。

今天的这篇文章为大家分享的是如何组织列表。很多时候，我们需要控制列表内元素的顺序，有时候你可能希望，保留列表元素最初的排列顺序，而有时候又需要调整排列顺序。Python提供了很多组织列表的方式。

下面我就对他们进行一一说明。

# 使用方法sort()对列表进行永久排序

Python方法sort()可以较为简便的就可以对列表进行排序。假设有一个汽车的列表，并要让其中的汽车按照字母顺序进行排列。

具体代码，如下所示：

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

运行结果，如下所示：

```
['audi', 'bmw', 'subaru', 'toyota']
```

从上面的代码可以看到，已经永久性的修改了列表元素的顺序，现在汽车是按照字母顺序排列的，再也无法恢复到原来的排列顺序了。

还可以按照字母顺序相反顺序排列列表元素，只需要向sort()方法传递参数reverse=True即可。下面示例将汽车列表按与字母顺序相反的顺序排列。

具体代码如下所示：

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```

运行结果，如下所示：

```
['toyota', 'subaru', 'bmw', 'audi']
```

同样的，对列表排序的修改也是永久性的。

# 使用函数sorted()对列表临时排序

要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可以使用函数sorted()。函数sorted()让你能够按特定的顺序显示列表元素，同时不影响他们在列表中的原始排列顺序。

具体代码，如下所示：

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']


print('原始顺序')
print(cars)

print('修改后的顺序')
print(sorted(cars))

print('原始顺序')
print(cars)
```

运行结果，如下所示：

```
原始顺序
['bmw', 'audi', 'toyota', 'subaru']
修改后的顺序
['audi', 'bmw', 'subaru', 'toyota']
原始顺序
['bmw', 'audi', 'toyota', 'subaru']
```

使用sorted()函数对列表进行排序之后，列表的原始顺序是不会改变的。

同样的，也可以向函数sorted()传入参数reverse=True，即可按照字母顺序的相反顺序进行排列。

# 倒着打印列表

要反转元素的排列顺序，可以使用方法reverse()。

注意：这个方法并不是按着字母进行排序，而是将列表进行反转。

具体代码，如下所示：

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('反转前')
print(cars)


print('反转后')
cars.reverse()
print(cars)

```

运行结果，如下所示：

```
反转前
['bmw', 'audi', 'toyota', 'subaru']
反转后
['subaru', 'toyota', 'audi', 'bmw']
```

同样的方法reverse()也是永久的修改元素的排列顺序，但是也可以随时恢复原来的排列，只需要对列表再次reverse()即可。

# 确定列表长度

使用函数len()可以快速的获悉列表的长度。具体代码，如下所示：

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
```

运行结果，如下所示：

```
4
```

函数len()的使用频率是比较高的，可以快速统计列表元素的总数。

> 注意Python计算列表的长度时，是从1开始计算的，但是索引却是从0开始计算的，因此这里你会很容易造成索引错误。

# 使用列表时避免索引错误

每个新人学习列表的时候，都会遇到一种错误，就是索引错误。假如一个包含三个元素的列表，但是却要你获取第四个元素。

具体代码，如下所示：

```python
cars = ['bmw', 'audi', 'toyota']
print(cars[3])
```

运行结果，如下所示：

```
Traceback (most recent call last):
  File "demo6.py", line 2, in <module>
    print(cars[3])
IndexError: list index out of range
```

很明显出现了错误，超出了范围。意味着Python在指定索引处找不到元素。

别忘记了，在上一篇文章的时候说过，每当要访问最后一个元素时，可以使用索引-1。但是，当列表为空的时候，就会出现错误。

> 注意，当你出现索引错误的时候，不妨把列表打印出来，也许它可能与你所想的完全不同。

# 最后

没有什么事情是可以一蹴而就的，生活如此，学习亦是如此！

因此，哪里会有什么三天速成，七天速成的说法呢？

唯有坚持，方能成功！

**啃书君说**：

文章的每一个字都是我用心敲出来的，只希望对得起每一位关注我的人。在文章末尾点【**赞**】，让我知道，你们也在为自己的学习拼搏和努力。

**路漫漫其修远兮，吾将上下而求索**。

我是**啃书君**，一个专注于学习的人，**你懂的越多，你不懂的越多**。更多精彩内容，我们下期再见！