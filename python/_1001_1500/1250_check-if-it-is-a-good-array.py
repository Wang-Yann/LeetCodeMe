#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 14:57:33
# @Last Modified : 2020-07-05 14:57:33
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。 
# 
#  假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [12,5,7,23]
# 输出：true
# 解释：挑选数字 5 和 7。
# 5*3 + 7*(-2) = 1
#  
# 
#  示例 2： 
# 
#  输入：nums = [29,6,10]
# 输出：true
# 解释：挑选数字 29, 6 和 10。
# 29*1 + 6*(-3) + 10*(-1) = 1
#  
# 
#  示例 3： 
# 
#  输入：nums = [3,6]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^9 
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
    def isGoodArray(self, nums: List[int]) -> bool:
        """
        Chinese remainder theorem

        If a % x = 0 and b % x = 0,
        appareantly we have (pa + qb) % x == 0
        If x > 1, making it impossible pa + qb = 1.


        """
        return functools.reduce(math.gcd, nums)==1
        
# leetcode submit region end(Prohibit modification and deletion)



@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        nums = [12,5,7,23]
    ), True),
    pytest.param(dict(  nums = [29,6,10] ), True),
])
def test_solutions(kwargs, expected):
    assert Solution().isGoodArray(**kwargs) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

