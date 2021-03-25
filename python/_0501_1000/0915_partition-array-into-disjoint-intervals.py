#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得： 
# 
#  
#  left 中的每个元素都小于或等于 right 中的每个元素。 
#  left 和 right 都是非空的。 
#  left 要尽可能小。 
#  
# 
#  在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
#  
# 
#  示例 2： 
# 
#  输入：[1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 30000 
#  0 <= A[i] <= 10^6 
#  可以保证至少有一种方法能够按题目所描述的那样对 A 进行划分。 
#  
# 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        length = len(A)
        max_val = float("-inf")
        max_left = [0] * length
        for i in range(length):
            max_val = max(max_val, A[i])
            max_left[i] = max_val
        min_val = float("inf")
        min_right = [0] * length
        for i in range(len(A) - 1, -1, -1):
            min_val = min(min_val, A[i])
            min_right[i] = min_val
        # print( max_left,min_right)
        for i in range(1, length):
            if max_left[i - 1] <= min_right[i]:
                return i


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([5, 0, 3, 8, 6], 3),
    ([1, 1], 1),
    pytest.param([1, 1, 1, 0, 6, 12], 4),
])
def test_solutions(args, expected):
    assert Solution().partitionDisjoint(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
