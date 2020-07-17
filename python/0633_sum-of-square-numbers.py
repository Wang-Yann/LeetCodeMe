#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:14:35
# @Last Modified : 2020-05-05 17:14:35
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
#
#  示例1:
#
#
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#
#
#
#
#  示例2:
#
#
# 输入: 3
# 输出: False
#
#  Related Topics 数学
#  👍 124 👎 0

import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c))+1):
            b = int(math.sqrt(c-a**2))
            if a**2+b**2==c:
                return True
        return False

@pytest.mark.parametrize("args,expected", [
    (5, True),
    pytest.param(3,False),
])
def test_solutions(args, expected):
    assert Solution().judgeSquareSum(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


