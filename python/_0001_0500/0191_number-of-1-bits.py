#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
#  
# 
#  示例 2： 
# 
#  输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
#  
# 
#  示例 3： 
# 
#  输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。 
# 
#  
# 
#  提示： 
# 
#  
#  请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的
# 还是无符号的，其内部的二进制表示形式都是相同的。 
#  在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。 
#  
# 
#  
# 
#  进阶: 
# 如果多次调用这个函数，你将如何优化你的算法？ 
#  Related Topics 位运算

"""

import pytest


class Solution0(object):
    def hammingWeight(self, n):
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0F0F0F0F) + ((n >> 4) & 0x0F0F0F0F)
        n = (n & 0x00FF00FF) + ((n >> 8) & 0x00FF00FF)
        n = (n & 0x0000FFFF) + ((n >> 16) & 0x0000FFFF)
        return n


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        n = abs(n)
        while n:
            if n & 0b1:
                cnt += 1
            n >>= 1
        return cnt


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n - 1)
            cnt += 1
        return cnt


@pytest.mark.parametrize("args,expected", [
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution0, Solution1])
def test_solutions(args, expected, SolutionCLS):
    assert Solution().hammingWeight(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
