#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 11:14:37
# @Last Modified : 2020-07-27 11:14:37
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。 
# 
#  示例: 
# 
#  输入: nums = [3,5,2,1,6,4]
# 输出: 一个可能的解答是 [3,5,1,6,2,4] 
#  Related Topics 排序 数组 
#  👍 23 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (
                    i % 2 == 1 and nums[i] < nums[i + 1]
            ):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        med = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]


@pytest.mark.parametrize("nums,expected", [
    ([3, 5, 2, 1, 6, 4], [3, 5, 1, 6, 2, 4]),
])
def test_solutions(nums, expected):
    Solution().wiggleSort(nums)
    i = 1
    while i < len(nums) - 1:
        if i % 2 == 0:
            assert nums[i - 1] > nums[i] < nums[i + 1]
        else:
            assert nums[i - 1] < nums[i] > nums[i + 1]
        i += 1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
