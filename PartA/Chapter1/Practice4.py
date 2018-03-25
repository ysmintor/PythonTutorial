"""
今天习题

1：

a = 'pyer'

b = 'apple'

用字典和format方法实现：

my name is pyer, i love apple.


2:打开文件info.txt,并且写入500这个数字。

"""

a = 'pyer'
b = 'apple'

ans1 = "my name is %s, i love %s" % (a, b)
ans2 = "my name is {who}, i love {fruit}".format(who=a, fruit="b")
ans3 = "my name is %(who)s, i love %(fruit)s" % {"who":a, "fruit":b}
print(ans1)
print(ans2)
print(ans3)


file1 = open("info.txt", "w")
file1.write("500")
file1.close()

file2 = open("info.txt", 'r')
line = file2.readline()
print(line)


