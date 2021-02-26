#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 06:31:10
# @Last Modified : 2021-02-26 06:31:10
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。 
# 
#  返回 只删除一个 子数组可获得的 最大得分 。 
# 
#  如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,2,4,5,6]
# 输出：17
# 解释：最优子数组是 [2,4,5,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,2,1,2,5,2,1,2,5]
# 输出：8
# 解释：最优子数组是 [5,2,1] 或 [1,2,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 104 
#  
#  Related Topics 双指针 
#  👍 20 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """AC"""
        N = len(nums)
        l = 0
        window = set()
        ans = cur = 0
        for r in range(N):
            while nums[r] in window:
                window.remove(nums[l])
                cur -= nums[l]
                l += 1
            window.add(nums[r])
            cur += nums[r]
            ans = max(ans, cur)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[4, 2, 4, 5, 6]), 17],
    [dict(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]), 8],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maximumUniqueSubarray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
