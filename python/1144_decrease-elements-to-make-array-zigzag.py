#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。 
# 
#  如果符合下列情况之一，则数组 A 就是 锯齿数组： 
# 
#  
#  每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ... 
#  或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ... 
#  
# 
#  返回将数组 nums 转换为锯齿数组所需的最小操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,6,1,6,2]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 1000 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        wo options, either make A[even] smaller or make A[odd] smaller.
        Loop on the whole array A,
        find the min(A[i - 1],A[i + 1]),
        calculate that the moves need to make smaller than both side.
        If it's negative, it means it's already smaller than both side, no moved needed.
        Add the moves need to res[i%i].
        In the end return the smaller option.

        """
        nums = [0x7fffffff] + nums + [0x7fffffff]
        res = [0, 0]
        for i in range(1, len(nums) - 1):
            res[i % 2] += max(0, nums[i] - (min(nums[i - 1], nums[i + 1]) - 1))
        # print(res)
        return min(res)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        ans1, ans2 = 0, 0
        for i in range(n):
            # 奇数位置
            if i % 2 == 0:
                d1 = nums[i] - (nums[i - 1] - 1) if i > 0 and nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - (nums[i + 1] - 1) if i < n - 1 and nums[i] >= nums[i + 1] else 0
                ans1 += max(d1, d2)
            # 偶数位置
            else:
                d1 = nums[i] - (nums[i - 1] - 1) if nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - (nums[i + 1] - 1) if i < n - 1 and nums[i] >= nums[i + 1] else 0
                ans2 += max(d1, d2)
        return min(ans1, ans2)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3], 2),
    pytest.param([9, 6, 1, 6, 2], 4),
])
def test_solutions(args, expected):
    assert Solution().movesToMakeZigzag(args) == expected
    assert Solution1().movesToMakeZigzag(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
