#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 23:47:08
# @Last Modified : 2020-07-12 23:47:08
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。 
# 
#  示例1: 
# 
#  
#  输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
#  输出：2
#  
# 
#  示例2: 
# 
#  
#  输入：A = 1，B = 2
#  输出：2
#  
# 
#  提示: 
# 
#  
#  A，B范围在[-2147483648, 2147483647]之间 
#  
#  Related Topics 位运算 
#  👍 8 👎 0


"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE,BIG_RES







# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        res = 0
        c = A ^ B
        for i in range(32):
            res += c >> i & 1
        return res

# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(      A = 29, B = 15                          ), 2],

    pytest.param(dict(        A = 1,B = 2             ), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().convertInteger(**kwargs) == expected







if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

