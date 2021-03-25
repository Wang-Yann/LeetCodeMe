#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 15:08:43
# @Last Modified : 2020-07-29 15:08:43
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。 
# 
#  示例 1： 
# 
#  输入：[1,0,1,1,0]
# 输出：4
# 解释：翻转第一个 0 可以得到最长的连续 1。
#      当翻转以后，最大连续 1 的个数为 4。
#  
# 
#  
# 
#  注： 
# 
#  
#  输入数组只包含 0 和 1. 
#  输入数组的长度为正整数，且不超过 10,000 
#  
# 
#  
# 
#  进阶： 
# 如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？ 
#  Related Topics 双指针 
#  👍 25 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        GOOD
        定义 dp[i][0]  为考虑到以 i 为结尾未使用操作将 [0,i] 某个 0 变成 1 的最大的连续 1 的个数，
        dp[i][1] 为考虑到以 i 为结尾使用操作将 [0,i] 某个 0 变成 1 的最大的连续 1 的个数

        """
        N = len(nums)
        ans = dp0 = dp1 = 0
        for i in range(N):
            if nums[i] == 1:
                dp0 += 1
                dp1 += 1
            else:
                dp1 = dp0 + 1
                dp0 = 0
            ans = max(dp0, dp1, ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 0, 1, 1, 0]), 4],
])
def test_solutions(kw, expected):
    assert Solution().findMaxConsecutiveOnes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
