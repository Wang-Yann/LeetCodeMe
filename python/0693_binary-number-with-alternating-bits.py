#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。 
# 
#  示例 1: 
# 
#  
# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
#  
# 
#  示例 2: 
# 
#  
# 输入: 7
# 输出: False
# 解释:
# 7的二进制数是: 111
#  
# 
#  示例 3: 
# 
#  
# 输入: 11
# 输出: False
# 解释:
# 11的二进制数是: 1011
#  
# 
#  示例 4: 
# 
#  
# 输入: 10
# 输出: True
# 解释:
# 10的二进制数是: 1010
#  
#  Related Topics 位运算

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n:
            bit = n & 0b1
            n >>= 1
            if bit == prev:
                return False
            prev = bit
        return True


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (5, True),
    (7, False),
    (11, False),
    (10, True),
])
def test_solutions(args, expected):
    assert Solution().hasAlternatingBits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
