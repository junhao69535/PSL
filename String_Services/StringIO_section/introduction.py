#!coding=utf-8

# 这个模块实现了类文件对象：StringIO，用于读取或写入一个字符串缓存（也叫内存文件）
# 当你使用某个包的函数, 该函数需要文件对象作为操作对象, 而你并不想使用文件而是使用
# 字符串来代替的时候. 举例, pdfminer模块一些方法(最基础的打开pdf文件操作)需要使用
# 文件对象进行读取read和文件指针定位seek, 但我想使用网络的pdf数据存到内存作为输入,
# 不想写到硬盘. 这时StringIO就起作用了.
# 简而言之, 已有的方法/函数需要文件对象(尤其内部会调用文件对象的方法), 但只想用
# 字符串代替, 就可以用StringIO.

# class StringIO.StringIO([buffer])
"""
    当一个StringIO对象被创建，它能通过传递string给构造器来初始化一个已经存在的字符串。如果没有给
    字符串，StringIO将以空开始，同时初始文件位置也从0开始。

    StringIO对象既能接受Unicode也能8比特字符串，但两者混合一起用需要注意。如果两者一起用，则无法
    解释为7位ASCII（使用第8位）的8位字符串将在getvalue()调用时引发UnicodeError异常。
"""

# 下面关于StringIO对象的方法需要注意：

# StringIO.getvalue()
"""
    在StringIO对象调用close()方法之前，这个方法在任何时间能获取文件的所有内容。混合Unicode和8位
    字符串将抛出UnicodeError异常。
"""

# StringIO.close()
"""
    释放内存缓存。调用该方法后还调用其他方法将会抛出ValueError异常。
"""

import StringIO

output = StringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'  # 把'Second line.'重定向写入output

# Retrieve file contents -- this will be 'First line.\nSecond line.\n'
contents = output.getvalue()
print contents

# close object and discard memory buffer -- getvalue() will now raise an exception
output.close()

