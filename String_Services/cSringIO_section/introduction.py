#!coding=utf-8

"""
这个模块提供了和StringIO相似的接口，但更快。
"""

# cStringIO.StringIO([s])
"""
    返回一个类StringIO流用于读写。
    因为这是一个返回内置类型对象的工厂函数，因此没有办法通过继承来构建自己的版本。
    和StringIO不同的是，这个模块不能接收Unicode字符串，因为那不能被编码成纯ASCII字符串。
    其他不同的是，传一个字符串参数来调用StringIO()
"""