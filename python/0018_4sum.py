#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 14:59:18
# @Last Modified : 2020-04-06 14:59:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
#  注意：
#
#  答案中不可以包含重复的四元组。
#
#  示例：
#
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
#  Related Topics 数组 哈希表 双指针
#  👍 517 👎 0

"""
import collections
from typing import List

#
import pytest


class Solution:

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res


class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  i j k
        nums.sort()
        length = len(nums)
        res = []
        i = 0
        while i < length - 3:
            if i and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < length - 2:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                v_sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] < v_sum:
                        left += 1
                    elif nums[left] + nums[right] > v_sum:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left, right = left + 1, right - 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                j += 1
            i += 1
        return res


# Space: O(n^2)
class Solution2(object):
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                lookup[nums[i] + nums[j]].append([i, j])

        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and \
                            b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[-1, 0, 1, 2, -1, -4], target=0), [[-1, -1, 0, 2]]],
    [dict(nums=[1, 0, -1, 0, -2, 2], target=0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]],
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution, Solution1, Solution2
])
def test_solutions(kw, expected, SolutionCLS):
    assert sorted(SolutionCLS().fourSum(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
