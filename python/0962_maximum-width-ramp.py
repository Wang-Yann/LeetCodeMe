#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 A，坡是元组 (i, j)，其中 i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。 
# 
#  找出 A 中的坡的最大宽度，如果不存在，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[6,0,8,2,1,5]
# 输出：4
# 解释：
# 最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
#  
# 
#  示例 2： 
# 
#  输入：[9,8,1,0,1,9,4,0,4,1]
# 输出：7
# 解释：
# 最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 50000 
#  0 <= A[i] <= 50000 
#  
# 
#  
#  Related Topics 数组

"""

from typing import List

import pytest

from sample_datas import BIG_CASE


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        m = 0x7fffffff
        sorted_index = sorted(range(len(A)), key=A.__getitem__)
        # print(sorted_index)
        for i in sorted_index:
            ans = max(ans, i - m)
            m = min(m, i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def maxWidthRamp(self, A: List[int]) -> int:
        """TLE"""
        N = len(A)
        window = 0
        for l, v in enumerate(A):
            r = N - 1
            while r - l + 1 >= window and A[r] < v:
                r -= 1
            window = max(window, r - l)
        return window


@pytest.mark.parametrize("args,expected", [
    ([6, 0, 8, 2, 1, 5], 4),
    ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7),
    (BIG_CASE.BIG_0962, 5),
])
def test_solutions(args, expected):
    assert Solution().maxWidthRamp(args) == expected
    assert Solution1().maxWidthRamp(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
