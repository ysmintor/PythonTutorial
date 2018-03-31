#coding=utf-8
"""
一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。
"""

s = "i,am,lilei"
print(s[2:4])
print(s.split(",")[1])

"""
二.在python中，如何修改字符串？
"""
ainfo = 'i love php'
replycontent = ainfo.replace('php','python')
print(replycontent)

"""
三.bool("2012" == 2012) 的结果是什么。
"""
print(bool("2012" == 2012))

"""
四.已知一个文件 test.txt，内容如下：

____________
2012来了。
2012不是世界末日。
2012欢乐多。
_____________

1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。
6.请取出最后2个字符。
7.请从字符串的最初开始，截断该字符串，使其长度为11.
8.请将{4}中的字符串保存为test1.py文本.
 
"""
#1.请输出其内容。
f = open('test.txt', 'r', encoding='UTF-8')
content = f.read()
print(content)
#2.请计算该文本的原始长度。
print(len(content))
#3.请去除该文本的换行。
print(content.replace('\n', ''))
#4.请替换其中的字符"2012"为"2013"。
print(content.replace("2012","2013"))
#5.请取出最中间的长度为5的子串。
contentlengh = len(content)
print(content[int(contentlengh / 2): int(contentlengh / 2) + 5])
#6.请取出最后2个字符。
print(content[-2:])
#7.请从字符串的最初开始，截断该字符串，使其长度为11.
print(content[:11])
#8.请将{4}中的字符串保存为test1.py文本.
filesave = open("test1.py", "w", encoding='utf-8')
filesave.write(content.replace('2012', '2013'))
filesave.close()


"""
五.请用代码的形式描述python的引用机制。
"""

chinese = "中文"
print("id of a = " + str(id(chinese)))
import sys
print(sys.getrefcount("中文"))
chinese = 1002
print("id of a = " + str(id(chinese)))
print("ref count "  + str(sys.getrefcount("中文")))


"""
六.已知如下代码

________

a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
________

1.请给出str对象"中文编程"的引用计数
2.请给出str对象"python编程"的引用计数
"""
a = "中文编程"
print("a:%s" % id(a))
b = a
print("b:%s" % id(b))
c = a
print("c:%s" % id(c))
print(sys.getrefcount('中文编程'))
a = "python编程"
print("a:%s" % id(a))
b = u'%s' %a
print("b:%s" % id(b))
d = "中文编程"
print(sys.getrefcount('中文编程'))
e = a
print("e:%s" % id(e))
c = b
print("c:%s" % id(c))

b2 = a.replace("中","中")
print("b2:%s" % id(b2))

print('result-----------------')
print(sys.getrefcount('中文编程'))
print(sys.getrefcount('python编程'))

"""
七.已知如下变量
________
a = "字符串拼接1"
b = "字符串拼接2"
________

1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2.请将a与b拼接成字符串c，并用逗号分隔。
3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
"""

#1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
a = "字符串拼接1"
b = "字符串拼接2"

#method 1
method1 = "%s%s" % (a,b)
print(method1)
#method 2
method2 = "{str1}{str2}".format(str1=a, str2=b)  #方法推荐
print(method2)
#method 3
method3 = "%(str1)s%(str2)s" % {"str1":a, "str2":b}
print(method3)
#method 4
method4 = "".join([a,b])
print(method4)

#2.请将a与b拼接成字符串c，并用逗号分隔。
newjobin = "%s,%s" % (a, b)

print(newjobin)
print(len(newjobin))
print(newjobin[6])


"""
八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。
"""

import string
##1.包含0-9的数字。

#print help(string)
print(string.digits)

##2.所有小写字母。
print(string.ascii_lowercase)

##3.所有标点符号。
print(string.punctuation)

##4.所有大写字母和小写字母。
print(string.ascii_letters)

##5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。
print("".join([string.digits, string.ascii_lowercase, string.punctuation, string.ascii_letters]))

"""
九.已知字符串
________

a = "i,am,a,boy,in,china"
________

1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2.请使用2种办法取出其间的字符"boy"和"china"。
3.请找出第一个"i"出现的位置。
4.请找出"china"中的"i"字符在字符串a中的位置。
5.请计算该字符串一共有几个逗号。
"""
##1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
ac = "i,am,a,%(sex)s,in,%(country)s" % {"sex":"boy","country":"china"}
bc = "i,am,a,{sex},in,{country}".format(sex="boy",country="china")
print(ac)
print(bc)
##2.请使用2种办法取出其间的字符"boy"和"china"。
#method1
print(ac[7:10])
print(ac[-5:])
#mehtod2
splictworlds = ac.split(',')
print(splictworlds[3])
print(splictworlds[-1])

#3.请找出第一个"i"出现的位置。

print(ac.index('i'))
print(ac.find('i'))
#4.请找出"china"中的"i"字符在字符串a中的位置。
print(ac.index('i', ac.index('china')))
print(ac.rindex('i'))

#5.请计算该字符串一共有几个逗号。
print(ac.count(','))

"""
十.请将模块string的帮助文档保存为一个文件。
"""
import sys

f = open('test.log', 'w')
sys.stdout = f
help(string)
f.close()