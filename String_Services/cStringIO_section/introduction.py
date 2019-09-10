#!coding=utf-8

"""
这个模块提供了和StringIO相似的接口，但更快。
"""

# cStringIO.StringIO([s])
"""
    返回一个类StringIO流用于读写。
    因为这是一个返回内置类型对象的工厂函数，因此没有办法通过继承来构建自己的版本。
    
    和StringIO不同的是，这个模块不能接收Unicode字符串，因为那不能被编码成纯ASCII字符串。
    
    其他不同的是，传一个字符串参数来调用StringIO()只会生成一个只读对象，不像那些不传字符串
    参数的，它没有写方法。这些对象通常是不可见的。它们只会作为StringI和StringO出现在溯源中。
"""

# cStringIO.InputType
"""
    通过使用字符串参数调用StringIO()创建的对象的类型对象。
"""

# cStringIO.OutputType
"""
    通过不使用字符串参数调用StringIO()创建的对象的类型对象。
"""

# 关于这个模块的C API，请参考源吗

import cStringIO

output = cStringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

contents = output.getvalue()
print contents

output.close()

input = cStringIO.StringIO('this is a test')
try:
    input.write('this is another test')  # 不可写，会抛出异常
except:
    print input.getvalue()
    input.close()