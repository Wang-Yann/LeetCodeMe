#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 20:42:27
# @Last Modified : 2020-07-06 20:42:27
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 「无零整数」是十进制表示中 不含任何 0 的正整数。 
# 
#  给你一个整数 n，请你返回一个 由两个整数组成的列表 [A, B]，满足： 
# 
#  
#  A 和 B 都是无零整数 
#  A + B = n 
#  
# 
#  题目数据保证至少有一个有效的解决方案。 
# 
#  如果存在多个有效解决方案，你可以返回其中任意一个。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：[1,1]
# 解释：A = 1, B = 1. A + B = n 并且 A 和 B 的十进制表示形式都不包含任何 0 。
#  
# 
#  示例 2： 
# 
#  输入：n = 11
# 输出：[2,9]
#  
# 
#  示例 3： 
# 
#  输入：n = 10000
# 输出：[1,9999]
#  
# 
#  示例 4： 
# 
#  输入：n = 69
# 输出：[1,68]
#  
# 
#  示例 5： 
# 
#  输入：n = 1010
# 输出：[11,999]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 10^4 
#  
#  Related Topics 数学 
#  👍 12 👎 0

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
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n//2+1):
            if  "0" not in "{}{}".format(i,n-i):
                return [i,n-i]


        
# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(n = 2), [1,1]),
    pytest.param(dict( n = 11  ), [2,9]),
    pytest.param(dict( n = 10000  ), [1,9999]),
    pytest.param(dict( n = 69  ), [1,68]),
    pytest.param(dict( n = 1010  ), [11,999]),
])
def test_solutions(kwargs, expected):
    res = Solution().getNoZeroIntegers(**kwargs)
    for v in res:
        assert '0' not in str(v)








if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

