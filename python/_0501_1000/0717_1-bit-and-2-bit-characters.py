#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。 
# 
#  现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。 
# 
#  示例 1: 
# 
#  
# 输入: 
# bits = [1, 0, 0]
# 输出: True
# 解释: 
# 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# bits = [1, 1, 1, 0]
# 输出: False
# 解释: 
# 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
#  
# 
#  注意: 
# 
#  
#  1 <= len(bits) <= 1000. 
#  bits[i] 总是0 或 1. 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        贪心
        最后一位是否为一比特字符，只和他左侧出现的连续的 1 的个数（即它与倒数第二个 0 出现的位置之间的 1 的个数，
        如果 bits 数组中只有 1 个 0，那么就是整个数组的长度减一）有关
        如果 1 的个数为偶数个，那么最后一位是一比特字符，如果 1 的个数为奇数个，那么最后一位不是一比特字符
        """
        length = len(bits)
        parity = 0
        for bit in reversed(bits[:length - 1]):
            if bit == 0:
                break
            parity ^= bit
        return parity == 0


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    """
    当扫描到第 ii 位时，如果 bits[i]=1，那么说明这是一个两比特字符，将 i 的值增加 2。
    如果 bits[i]=0，那么说明这是一个一比特字符，将 i 的值增加 1

    """

    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 0], True),
    pytest.param([1, 1, 1, 0], False),
])
def test_solutions(args, expected):
    assert Solution().isOneBitCharacter(args) == expected
    assert Solution1().isOneBitCharacter(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
