#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组： 
# 
#  
#  若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]； 
#  或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。 
#  
# 
#  也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。 
# 
#  返回 A 的最大湍流子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
#  
# 
#  示例 2： 
# 
#  输入：[4,8,12,16]
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：[100]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 40000 
#  0 <= A[i] <= 10^9 
#  
#  Related Topics 数组 动态规划 Sliding Window

"""

from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
cmp = lambda a, b: a - b


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        res = 1
        start = 0
        for i in range(1, len(A)):
            c_pre = cmp(A[i - 1], A[i])
            if i == len(A) - 1 or c_pre * cmp(A[i], A[i + 1]) >= 0:
                if c_pre != 0:
                    res = max(res, i - start + 1)
                start = i
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
    ([4, 8, 12, 16], 2),
    ([100], 1),
    ([9, 9], 1),
])
def test_solutions(args, expected):
    assert Solution().maxTurbulenceSize(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
