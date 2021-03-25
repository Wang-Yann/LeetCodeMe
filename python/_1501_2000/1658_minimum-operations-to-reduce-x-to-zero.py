#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 09:30:35
# @Last Modified : 2021-02-25 09:30:35
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改
#  数组以供接下来的操作使用。 
# 
#  如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 104 
#  1 <= x <= 109 
#  
#  Related Topics 贪心算法 双指针 二分查找 Sliding Window 
#  👍 51 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        GOOD
        Sliding window: Longest subarray sum to the target = sum(nums) - x
        """
        target = sum(nums) - x
        N = len(nums)
        size, win_sum, l = -1, 0, -1
        for r, num in enumerate(nums):
            win_sum += num
            while l < N - 1 and win_sum > target:
                l += 1
                win_sum -= nums[l]
            if win_sum == target:
                size = max(size, r - l)
        return -1 if size == -1 else N - size


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 1, 4, 2, 3], x=5), 2],
    [dict(nums=[5, 6, 7, 8, 9], x=4), -1],
    [dict(nums=[3, 2, 20, 1, 1, 3], x=10), 5],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().minOperations(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
