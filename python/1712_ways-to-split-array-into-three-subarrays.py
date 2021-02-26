#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 10:18:16
# @Last Modified : 2021-02-26 10:18:16
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 我们称一个分割整数数组的方案是 好的 ，当它满足： 
# 
#  
#  数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。 
#  left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。 
#  
# 
#  给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 109 + 7 取余后返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1]
# 输出：1
# 解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,2,2,5,0]
# 输出：3
# 解释：nums 总共有 3 种好的分割方案：
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,2,1]
# 输出：0
# 解释：没有好的分割方案。 
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 105 
#  0 <= nums[i] <= 104 
#  
#  Related Topics 双指针 二分查找 
#  👍 35 👎 0


import bisect
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        Any at index i, you want to find index j such at
        prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]

        Key idea

        prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        ->
        2 * prefix[i] <= prefix[left_boundary]
        and
        2 * prefix[right_boundary] <= prefix[-1] + prefix[i]
        
        Once i is given, we can know left_boundary and right_boundary, and update answer by

        answer += right_boundary - left_boundary
        """
        MOD = 10 ** 9 + 7
        N = len(nums)
        prefix = list(itertools.accumulate(nums))
        ans = 0
        for i in range(N):
            l = max(i + 1, bisect.bisect_left(prefix, prefix[i] + prefix[i]))
            r = min(N - 1, bisect.bisect_right(prefix, (prefix[i] + prefix[-1]) // 2))
            ans = (ans + max(0, r - l)) % MOD
        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 1, 1]), 1],
    [dict(nums=[1, 2, 2, 2, 5, 0]), 3],
    [dict(nums=[3, 2, 1]), 0],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().waysToSplit(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
