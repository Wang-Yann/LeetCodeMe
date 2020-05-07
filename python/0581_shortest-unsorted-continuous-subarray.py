#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。 
# 
#  你找到的子数组应是最短的，请输出它的长度。 
# 
#  示例 1: 
# 
#  
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#  
# 
#  说明 : 
# 
#  
#  输入的数组长度范围在 [1, 10,000]。 
#  输入的数组可能包含重复元素 ，所以升序的意思是<=。 
#  
#  Related Topics 数组

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        length = len(nums)
        l, r = length, 0
        for i in range(length):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(length-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        if r - l > 0:
            return r - l + 1
        return 0

# leetcode submit region end(Prohibit modification and deletion)


class Solution1:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        a = sorted(nums)
        while nums[left] == a[left] or nums[right] == a[right]:
            if right - left <= 1:
                return 0
            if nums[left] == a[left]:
                left += 1
            if nums[right] == a[right]:
                right -= 1
        return right - left + 1


class Solution2:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -2
        min_from_right, max_from_left = nums[-1], nums[0]
        for i in range(1, n):
            max_from_left = max(max_from_left, nums[i])
            min_from_right = min(min_from_right, nums[n-1-i])
            if nums[i] < max_from_left: right = i
            if nums[n-1-i] > min_from_right: left = n-1-i
        return right-left+1


@pytest.mark.parametrize("args,expected", [
    ([2, 6, 4, 8, 10, 9, 15], 5),
    ([1, 2, 3, 4], 0),
    ([1, 3, 2, 2, 2], 4),
])
def test_solutions(args, expected):
    assert Solution().findUnsortedSubarray(args) == expected
    assert Solution1().findUnsortedSubarray(args) == expected
    assert Solution2().findUnsortedSubarray(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
