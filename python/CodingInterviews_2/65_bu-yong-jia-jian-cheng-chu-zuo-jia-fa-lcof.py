#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。 
# 
#  
# 
#  示例: 
# 
#  输入: a = 1, b = 1
# 输出: 2 
# 
#  
# 
#  提示： 
# 
#  
#  a, b 均可能是负数或 0 
#  结果不会溢出 32 位整数 
#  
# 

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def add(self, a: int, b: int) -> int:
        """
        https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/pythonti-jie-er-jin-zhi-zhuan-hua-yi-ji-pythonzhua/
            Python 负数的存储：
            Python / Java 中的数字都是以 补码 形式存储的。但 Python 没有 int , long 等不同长度变量，即没有变量位数的概念。
            获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。可理解为舍去此数字 3232 位以上的数字，从无限长度变为一个 3232 位整数。
            返回前数字还原： 若补码 aa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。 a ^ x 运算将 11 至 3232 位按位取反； ~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 3232 位以上的位取反，即由 00 变为 11 ， 11 至 3232 位不变。

            print(hex(1)) # = 0x1 补码
            print(hex(-1)) # = -0x1 负号 + 原码 （ Python 特色，Java 会直接输出补码）

            print(hex(1 & 0xffffffff)) # = 0x1 正数补码
            print(hex(-1 & 0xffffffff)) # = 0xffffffff 负数补码

            print(-1 & 0xffffffff) # = 4294967295 （ Python 将其认为正数）

        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b:
            # 计算进位值，得到 1010，相当于各位做与操作得到 101，再向左移一位得到 1010
            carry = ((a & b) << 1) & x
            # 二进制每位相加就相当于各位做异或操作
            a ^= b
            b = carry
        # 如果是正数的话直接返回
        if a <= 0x7fffffff:
            return a
        # 如果是负数,转换成补码形式

        return ~(a ^ x)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(a=1, b=1), 2),
    (dict(a=0, b=-4), -4),
    pytest.param(dict(a=-100, b=1000), 900),
])
def test_solutions(kwargs, expected):
    assert Solution().add(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
