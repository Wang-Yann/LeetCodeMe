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

import pytest


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  i j k
        nums.sort()
        N = len(nums)
        res = []
        i = 0
        while i < N - 3:
            if i and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < N - 2:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                v_sum = target - nums[i] - nums[j]
                left, right = j + 1, N - 1
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
class Solution1(object):
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
                        if a is not c and a is not d and b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)


class Solution0:
    """推导规律"""

    def twoSumTarget(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        lo, hi = start, len(nums) - 1
        res = []
        while lo < hi:
            sum_val = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if sum_val < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif sum_val > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res

    def threeSumTarget(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        res = []
        N = len(nums)
        i = start
        while i < N:
            tuples = self.twoSumTarget(nums, i + 1, target - nums[i])
            for tp in tuples:
                res.append([nums[i]] + tp)
            while i < N - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        N = len(nums)
        i = 0
        while i < N:
            tuples = self.threeSumTarget(nums, i + 1, target - nums[i])
            for tp in tuples:
                res.append([nums[i]] + tp)
            while i < N - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res


class Solution00:
    def nSumTarget(self, n, nums, start, target):
        res = []
        N = len(nums)
        if n == 2:
            lo, hi = start, N - 1
            while lo < hi:
                sum_val = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if sum_val < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif sum_val > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            i = start
            while i < N:
                tuples = self.nSumTarget(n - 1, nums, i + 1, target - nums[i])
                for tp in tuples:
                    res.append([nums[i]] + tp)
                while i < N - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(4, nums, 0, target)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[-1, 0, 1, 2, -1, -4], target=0), [[-1, -1, 0, 2]]],
    [dict(nums=[1, 0, -1, 0, -2, 2], target=0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]],
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution, Solution1, Solution0, Solution00
])
def test_solutions(kw, expected, SolutionCLS):
    assert sorted(SolutionCLS().fourSum(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
