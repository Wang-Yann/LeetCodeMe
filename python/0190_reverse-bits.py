#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 颠倒给定的 32 位无符号整数的二进制位。 
# 
#  
# 
#  示例 1： 
# 
#  输入: 00000010100101000001111010011100
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
#       因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。 
# 
#  示例 2： 
# 
#  输入：11111111111111111111111111111101
# 输出：10111111111111111111111111111111
# 解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
#       因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。 
# 
#  
# 
#  提示： 
# 
#  
#  请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的
# 还是无符号的，其内部的二进制表示形式都是相同的。 
#  在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -10737418
# 25。 
#  
# 
#  
# 
#  进阶: 
# 如果多次调用这个函数，你将如何优化你的算法？ 
#  Related Topics 位运算

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseBits(self, n: int) -> int:
        string = bin(n)
        if "-" in string:
            string = string[:3] + string[3:].zfill(32)[::-1]
        else:
            string = string[:2] + string[2:].zfill(32)[::-1]
        return int(string, 2)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1
            res |= (n & 0b1)
            n >>= 1
        return res


@pytest.mark.parametrize("args,expected", [
    (0b00000010100101000001111010011100, 0b00111001011110000010100101000000),
    (0b11111111111111111111111111111101, 0b10111111111111111111111111111111),
])
def test_solutions(args, expected):
    assert Solution().reverseBits(args) == expected
    assert Solution1().reverseBits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
