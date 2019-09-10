#!coding=utf-8

"""
    datetime模块支持类对dates和times简单和复杂的操作。在date和time算术支持下，关注于有效属性提取
    和输入格式化以及操纵的实现。对于相关函数，见time和calendar模块。

    date和time对象有两种类型："naive"和"aware"

    aware对象具有足够的适用算法和政治时间调整知识，例如时区和夏令时信息，以相对于其他知晓对象定位
    自身。知觉对象用于表示对解释1不开放的特定时刻。

    一个naive的对象不包含足够的信息来明确地相对于其他日期/时间对象定位自己。天真物体是代表协调世界时
    （UTC），当地时间还是其他某个时区的时间完全取决于程序，就像程序一样，特定数字是代表米，英里
    还是质量。天真的物体易于理解和使用，代价是忽略了现实的某些方面。

    对于需要aware对象的app，datetime和time对象有一个可选的失去信息属性，tzinfo,可以设置位抽象
    zeinfo类的子类的实例。tzinfo对象捕捉关于UTC时间的offset，时间名称和夏令时是否生效的信息。
    注意datetime模块不支持具体的tzinfo类。在任何详细程度都需要支持时区取决于应用程序。世界各地
    的时间调整规则更具政治性而非理性，并且没有适合每种应用的标准。
"""

# datetime模块有以下的常量：

# datetime.MINYEAR
"""
    date或者datetime对象支持的最小年份
"""

# datetime.MAXYEAR
"""
    date或者datetime对象支持的最大年份
"""