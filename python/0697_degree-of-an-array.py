#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。 
# 
#  你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。 
# 
#  示例 1: 
# 
#  
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释: 
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
#  
# 
#  注意: 
# 
#  
#  nums.length 在1到50,000区间范围内。 
#  nums[i] 是一个在0到49,999范围内的整数。 
#  
#  Related Topics 数组

"""

import collections
import sys
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        degree = max(counter.values())
        return min(last[v] - first[v] + 1 for v in counter if counter[v] == degree)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = collections.defaultdict(list)
        for idx, v in enumerate(nums):
            counter[v].append(idx)
        degree = max(map(len, counter.values()))
        if degree == 1:
            return 1
        ans = sys.maxsize
        for num, idx_list in counter.items():
            if len(idx_list) == degree:
                ans = min(idx_list[-1] - idx_list[0] + 1, ans)
        return ans


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 2, 3, 1], 2),
    ([1, 2, 2, 3, 1, 4, 2], 6),
    ([3], 1),
    ([1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2], 9),
])
def test_solutions(args, expected):
    assert Solution().findShortestSubArray(args) == expected
    assert Solution1().findShortestSubArray(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
