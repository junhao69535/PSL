#!coding=utf-8

# 这个模块提供类和函数用于序列对比。它能对比文件，且能产生各种格式不同的信息，包括HTML和文本以及统一差异
# 对于对比目录和文件，可以参考filecmp模块。

# class difflib.SequenceWatcher
"""
    这是一个对比任何类型序列对的便捷的类，只要序列中的元素都是可哈希的。基本算法比1980年代后期由Ratcliff
    和Obershelp以双曲线名称“格式塔模式匹配”发布的算法更早，并且更加迷人。想法是找到不包含“垃圾”元素的最长
    的连续匹配子序列（Ratcliff和Obershelp算法不解决垃圾问题）。然后，相同的想法被递归地应用于匹配子序列的
    左侧和右侧的序列片段。这不会产生最小的编辑序列，但确实会产生对人们“看起来正确”的匹配。

    时间：基本的Ratcliff-Obershelp算法在最坏情况下是立方时间，在预期情况下是二次时间。SequenceMatcher对
    于最坏情况，它是二次时间，并且具有预期情况行为，其依赖于序列共有多少元素的复杂方式; 最佳案例时间是线性的。

    自动垃圾启发式： SequenceMatcher支持启发式，可自动将某些序列项视为垃圾。启发式计算每个单独项目在序列中
    出现的次数。如果项目的重复项（在第一项之后）占序列的1％以上且序列长度至少为200项，则此项目将标记为“热门”，
    并且为了序列匹配而被视为垃圾。可以通过在创建时设置autojunk参数来关闭此启发式。FalseSequenceMatcher
"""