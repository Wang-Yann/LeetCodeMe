#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 A，对于每个整数 A[i]，我们可以选择处于区间 [-K, K] 中的任意数 x ，将 x 与 A[i] 相加，结果存入 A[i] 。 
# 
#  在此过程之后，我们得到一些数组 B。 
# 
#  返回 B 的最大值和 B 的最小值之间可能存在的最小差值。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
#  
# 
#  示例 2： 
# 
#  输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
#  
# 
#  示例 3： 
# 
#  输入：A = [1,3,6], K = 3
# 输出：0
# 解释：B = [3,3,3] 或 B = [4,4,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  0 <= K <= 10000 
#  
#  Related Topics 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_val, min_val = max(A), min(A)
        if max_val - min_val <= 2 * K:
            return 0
        return max_val - min_val - 2 * K


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=[1], K=0), 0),
    pytest.param(dict(A=[0, 10], K=2), 6),
    pytest.param(dict(A=[1, 3, 6], K=3), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().smallestRangeI(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
