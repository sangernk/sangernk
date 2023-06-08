# 列表转字典
i = ['a', 'b', 'c', 'd']
j = [1, 2, 3, 4]
dic = dict(zip(i, j))  # 两个列表合并转字典
print(dic)
#########################################


###########################################
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
rev = list(zip(prices.values(), prices.keys()))
print(rev)
print(min(rev))
print(max(prices.values()))

##############################
# 利用集合去重
a = [1, 5, 6, 7, 2, 1, 5, 6, 9]
a_set = set(a)
a = list(a_set)
print(a)

#########################################
# slice()函数创建一个slice对象，该对象可用于对字符串，列表，元组等进行切片
my_slice = slice(5)  # class slice(object)  slice是类。   Create a slice object
my_slice2 = slice(2, 10, 2)
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = range(9)
print(arr[my_slice])  # [0, 1, 2, 3, 4]
print(arr[my_slice2])  # [2, 4, 6, 8]
print(my_slice.start, my_slice.stop, my_slice.step)
print(my_slice2.start, my_slice2.stop, my_slice2.step)

# '0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
# cost = int(record[20:23]) * float(record[31:37])
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
#########################################


#  ######################################  查找出现最多的单词
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
         'around', 'the', 'around', 'eyes', "do", 'my', 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes',
         "you", 'under'
         ]
a_set = set(words)  # 集合去重
a_list = list(a_set)
count = []  # 存放对应元素的数量
for i in a_list:
    count.append(words.count(i))
aa_list = list(zip(a_list, count))
print(max(aa_list, key=lambda x: x[1]))  # max 也是高阶函数 ，key 接收 func 类型

d = dict.fromkeys(a_set)  # 第二种 通过集合创建 None 值字典
for i in a_set:
    d[i] = words.count(i)
count = 0
for i in d:  # 遍历字典，找到最大值
    if d[i] > count:
        count = d[i]
        d_max = i, d[i]  # d_max 存储最大值信息
print(d_max)
# print(max(d.items(), key=lambda x: x[1]))  # 亦可不用for循环遍历寻找最大值，用 max 高阶函数
#############################################


mylist = [1, 4, -5, 10, -7, 2, 3, -1]
a_list = [x for x in mylist if x > 0]  # 只保留大于 0 的数
b_list = [x for x in mylist if x % 2]  # 只保留奇数
print(a_list, b_list)

######################################
values = ['1', '2', '-3', '-', '2.6', '4', 'N/A', '5', 6]


def is_int(x):
    try:
        int(x)
        return True
    except Exception:
        return False


result = list(filter(is_int, values))  # ['1', '2', '-3', '4', '5']
print(result)

nl = [x for x in values if isinstance(x, int)]  # 如果用 isinstance 判断，'1' 这样的是字符串类型，无法判断
print(nl)
##################################


##################################
mylist = [1, 4, -5, 10, -7, 2, 3, -1, 0]
import math

sq = [format(math.sqrt(x), '0.3f') for x in mylist if x >= 0]
print(sq)
##################################


##################################
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
counter = 0
for i in counts:
    if i > 5:  # 删选出 counts 大于5的地址
        print(addresses[counter], i)
    # msg = [addresses[counter], ''][i < 5]
    # print(msg)
    counter += 1
##################################


a, b = 4.2, 2.1
print(a + b)  # 6.300000000000001

from decimal import Decimal

a1, b1 = Decimal('4.2'), Decimal('2.1')
print(a1 + b1)  # 6.3

a, b = 4.2, 2.1
a, b = str(a), str(b)
a = a.split('.')
b = b.split('.')
for i in (a, b):
    print(i)
print(a, b)
########################################################


#########################################################
from fractions import Fraction

a, b = Fraction(1, 3), Fraction(2, 5)  # 分数  1/3   2/5
print(a + b)  # 11/15
print(a - b)  # -1/15
c = a * b  # 2/15
print(c, c.numerator, c.denominator)  # numerator 分子，denominator 分母

########################################################


#######################################  字典翻转，价格如有相同的，后面的会覆盖前面的
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}
new_ = {v: k for k, v in prices.items()}  # {45.23: 'ACME', 612.78: 'AAPL', 205.55: 'IBM', 37.2: 'HPQ', 10.75: 'FB'}
print(max(new_))
print(min(new_))
#########################################

lst = [1]
print(lst.count(2))  # 0

print(format(2.1, '7.02f'))  # ‘   2.10’
print(format(5, '05d'))  # 00005
print(format('Hello', '*^10'))  # **Hello***

print('{:*^10s} {:>10s}'.format('Hello', 'World'))  # **Hello***      World

print('hello'  ' '  'world')  # 'hello world'
my_str = '1' '.' '23'  # '1.23'
print(my_str)

lst1 = [1, 2]
lst2 = ['a', 'b']
lst_a = lst1 + lst2  # [1, 2, 'a', 'b']
print(lst_a)


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


print(' '.join(sample()))  # Is Chicago Not Chicago?

################################################
s = '{name} has {n} messages.'


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

    def say(self):
        print(f"俺名叫{self.name}")


a = Info("王大锤", 26)
# print(a)
print(s.format_map(vars(a)))
print(vars(a))  # 返回对象 a 的属性和属性值所组成的字典


class Stu:
    def __init__(self, name, age=0):
        self.name = name  # 成员变量前加 self
        self.age = age
        print(f"构造方法 init() {self.name} 已经运行")

    def __str__(self):
        return f"Stu类，name{self.name}.通过 __str__ 方法返回"

    def say_hi(self, msg=''):  # msg 不是成员变量，不加self
        print(f"Hi, I am {self.name}。{msg}")


print("-------->下面还是创建类")
stu1, stu2 = Stu("王大锤"), Stu("刘德华")
print("<--------创建类 结束")
Stu.say_hi(stu1, "今天请大家吃火锅")
stu2.say_hi("我给大家唱首歌")
print(stu1)  # 打印对象时，调用__str__方法
##########################################


###########################################
a_str = ['错的', '对的'][2 > 3]
b_str = ['错的', '对的'][2 < 3]
print(a_str, b_str)  # 错的 对的
print(type(a_str))  # <class 'str'>

# 两个列表并排在一起，右边是一个条件判断，左边是根据条件判断而执行或返回的两段内容

c_str = ['a', 'b', 'c'][2 < 3]
print(c_str)  # b

lst1 = list("tomcat")
lst2 = list("Jese")
shoter = [len(lst1), len(lst2)][len(lst1) > len(lst2)]
print(shoter)

import getpass

pwd = getpass.getpass("输入密码：")
print(pwd)

##############################################


############################
a = 'hHi KLPgf'
print(a.casefold())  # hhi klpgf    .casefold不需要任何参数  返回值是适合无条件比较的字符串
print("der Fluß".casefold())  # der fluss  德语小写字母ß 等效于ss
print("der Fluss".casefold())  # der fluss


##############################


########################################
class ReprStr:
    def __repr__(self):  # 命令行交互环境，输入对象名 回车，调用此方法。   字符串真正的样子
        return "返回的是 __repr__ 方法"

    def __str__(self):  # 用 print 输出变量时，调用此方法。   经过Python优化，更便于人类阅读的样式
        return "返回的是 __str__ 方法"


reprstr = ReprStr()
print(reprstr)  # 返回的是 __str__ 方法
##################################################


#########################################
import itertools

print(list(itertools.repeat(10, 6)))
print(list(itertools.repeat("哈", 6)))

for i in itertools.count(5, 3):  # count(初值=0, 步长=1)  count 迭代器会返回从传入的起始参数开始的均匀间隔的数值
    print(i)
    if i > 10:
        break

# print(list(itertools.cycle('abc')))  # 死循环，导致死机
################################################

text = '1aa2'
print(text.split('a'))  # ['1', '', '2']
print(text.split('aa'))  # ['1', '2']
#################################################


##################################################
import time

for i in range(100):
    print(i, end='\r')
    time.sleep(0.1)
with open("0.txt", "r") as f:  # 注意, 是__enter__()方法的返回值赋值给了my_file,
    # for line in f.readlines():
    #   print(line)
    data = f.read()
    print(data)
print()
######################################


###########################################
# 字典是无序类型，没有sort排序方法
d_1 = {'zj': 24, 'lj': 35, 'yz': 28}
nd = sorted(d_1.items(), key=lambda x: x[1])  # [('zj', 24), ('yz', 28), ('lj', 35)]
# 可迭代对象不要用字典d_1，那样只能迭代出的字典的键。要用d_1.items()才可迭代出字典的键值对
# nd = sorted(d_1.keys())  # 按照键排序  ['lj', 'yz', 'zj']
# nd = sorted(d_1.values())  # [24, 28, 35]
print(nd)

# 字典转列表
# L = list(d_1)  # ['zj', 'lj', 'yz']  只有键转为字典
L = list(d_1.items())  # [('zj', 24), ('lj', 35), ('yz', 28)]
L.sort(key=lambda x: x[1])  # [('zj', 24), ('yz', 28), ('lj', 35)]  转为列表后排序
print(L)

a = [(27, 35), (74, 55), (38, 55), (85, 55), (36, 58)]
a.sort(key=lambda x: (x[1], x[0]))  # 两个排序键
print(a)  # [(27, 35), (38, 55), (74, 55), (85, 55), (36, 58)]  # 3个的第二个元素相同，第一个元素是从大到小

