#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr 和一个整数 difference，请你找出 arr 中所有相邻元素之间的差等于给定 difference 的等差子序列，并返回其中
# 最长的等差子序列的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,2,3,4], difference = 1
# 输出：4
# 解释：最长的等差子序列是 [1,2,3,4]。 
# 
#  示例 2： 
# 
#  输入：arr = [1,3,5,7], difference = 1
# 输出：1
# 解释：最长的等差子序列是任意单个元素。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
# 输出：4
# 解释：最长的等差子序列是 [7,5,3,1]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -10^4 <= arr[i], difference <= 10^4 
#  
#  Related Topics 数学 动态规划

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lookup = collections.Counter()
        res = 1
        for i in range(len(arr)):
            v = arr[i]
            lookup[v] = lookup[v - difference] + 1
            res = max(res, lookup[v])
        # print(lookup)
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 2, 3, 4], difference=1), 4],
    [dict(arr=[1, 3, 5, 7], difference=1), 1],
    [dict(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2), 4],
])
def test_solutions(kw, expected):
    assert Solution().longestSubsequence(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
