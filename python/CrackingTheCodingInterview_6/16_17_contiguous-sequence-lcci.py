#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:05:13
# @Last Modified : 2020-07-13 18:05:13
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组，找出总和最大的连续数列，并返回总和。 
# 
#  示例： 
# 
#  输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶： 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 27 👎 0

"""
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res = max_sofar = -math.inf
        for v in nums:
            max_sofar = max(max_sofar+v , v)
            max_res = max(max_sofar, max_res)
        return max_res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6],
    [dict(nums=[-1]), -1],
])
def test_solutions(kw, expected):
    assert Solution().maxSubArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
