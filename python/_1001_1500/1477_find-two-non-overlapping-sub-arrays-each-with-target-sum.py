#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 arr 和一个整数值 target 。 
# 
#  请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。 
# 
#  请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,2,4,3], target = 3
# 输出：2
# 解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
#  
# 
#  示例 2： 
# 
#  输入：arr = [7,3,4,7], target = 7
# 输出：2
# 解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
#  
# 
#  示例 3： 
# 
#  输入：arr = [4,3,2,6,2,3,4], target = 6
# 输出：-1
# 解释：我们只有一个和为 6 的子数组。
#  
# 
#  示例 4： 
# 
#  输入：arr = [5,5,4,4,5], target = 3
# 输出：-1
# 解释：我们无法找到和为 3 的子数组。
#  
# 
#  示例 5： 
# 
#  输入：arr = [3,1,1,1,5,1,2,1], target = 3
# 输出：3
# 解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  1 <= arr[i] <= 1000 
#  1 <= target <= 10^8 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
         dp数组存放当前位置之前最短的一个长度
        """
        prefix = {0:-1}
        N = len(arr)
        dp = [0] * N
        res = min_len = 0x7fffffff
        accu = 0
        for right in range(N):
            accu += arr[right]
            prefix[accu] = right
            if accu - target in prefix:
                left = prefix[accu - target]
                min_len = min(min_len, right - left)
                if left != -1:
                    res = min(res, dp[left] + (right - left))
            dp[right] = min_len
        # print(dp)
        return res if res != 0x7fffffff else -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(arr=[3, 2, 2, 4, 3], target=3), 2),
    pytest.param(dict(arr=[7, 3, 4, 7], target=7), 2),
    pytest.param(dict(arr=[4, 3, 2, 6, 2, 3, 4], target=6), -1),
    pytest.param(dict(arr=[5, 5, 4, 4, 5], target=3), -1),
    pytest.param(dict(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().minSumOfLengths(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
