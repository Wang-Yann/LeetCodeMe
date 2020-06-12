#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 14:59:18
# @Last Modified : 2020-04-06 14:59:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针

"""

from typing import List

import pytest


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        i = 0
        while i < length - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, length - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return res

    def threeSum0(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        length = len(nums)
        res = []
        for i in range(0, length):
            v_i = nums[i]
            if v_i > 0:
                break
            for j in range(i + 1, length):
                v_j = nums[j]
                sum_ij = v_i + v_j
                if sum_ij > 0:
                    break
                for k in range(j + 1, length):
                    if sum_ij + nums[k] > 0:
                        break
                    if sum_ij + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in res:
                            res.append([nums[i], nums[j], nums[k]])

        return list(res)


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


@pytest.mark.parametrize("args,expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([1, -2, -5, -13, -10, -11, 0, -12, -11, 13, -4, 9, 8, 10, -7, 3, -9, -12, -7, 8, -2, -12, 1, -10, -15, -8,
      5, 14, -7, -8, -8, 9, -3, -6, 3, -5, -1, -11, -10, 3, -13, 1, -10, 3, -12, -10, -9, -13, -7, -1, 10, 6, -6, -12,
      12, -13, -13, -6, -14, -13, -7, -7, 4, 6, -6, -8, 8, 8, -4, 13, -11, -1, -8, -14, 9, -5, -9, 7, -3, -1, 14, 14,
      13, -7, 9, 2, -5, 12, 11, -12, 14, -11, -12, 3, 2, -2, 3, -5, -9, 14, -14, -13, -10, -7, -12, 14, 3, -6, -1, 8,
      1, -2, -1, -1, 6, -6],
     [[-15, 1, 14], [-15, 2, 13], [-15, 3, 12], [-15, 4, 11], [-15, 5, 10], [-15, 6, 9], [-15, 7, 8], [-14, 0, 14],
      [-14, 1, 13], [-14, 2, 12], [-14, 3, 11], [-14, 4, 10], [-14, 5, 9], [-14, 6, 8], [-13, -1, 14], [-13, 0, 13],
      [-13, 1, 12], [-13, 2, 11], [-13, 3, 10], [-13, 4, 9], [-13, 5, 8], [-13, 6, 7], [-12, -2, 14], [-12, -1, 13],
      [-12, 0, 12], [-12, 1, 11], [-12, 2, 10], [-12, 3, 9], [-12, 4, 8], [-12, 5, 7], [-12, 6, 6], [-11, -3, 14],
      [-11, -2, 13], [-11, -1, 12], [-11, 0, 11], [-11, 1, 10], [-11, 2, 9], [-11, 3, 8], [-11, 4, 7], [-11, 5, 6],
      [-10, -4, 14], [-10, -3, 13], [-10, -2, 12], [-10, -1, 11], [-10, 0, 10], [-10, 1, 9], [-10, 2, 8], [-10, 3, 7],
      [-10, 4, 6], [-9, -5, 14], [-9, -4, 13], [-9, -3, 12], [-9, -2, 11], [-9, -1, 10], [-9, 0, 9], [-9, 1, 8],
      [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, -6, 14], [-8, -5, 13], [-8, -4, 12], [-8, -3, 11], [-8, -2, 10],
      [-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-7, -7, 14], [-7, -6, 13], [-7, -5, 12],
      [-7, -4, 11], [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], [-7, 0, 7], [-7, 1, 6], [-7, 2, 5], [-7, 3, 4],
      [-6, -6, 12], [-6, -5, 11], [-6, -4, 10], [-6, -3, 9], [-6, -2, 8], [-6, -1, 7], [-6, 0, 6], [-6, 1, 5],
      [-6, 2, 4], [-6, 3, 3], [-5, -5, 10], [-5, -4, 9], [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], [-5, 1, 4],
      [-5, 2, 3], [-4, -4, 8], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-3, -3, 6],
      [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-2, 1, 1], [-1, -1, 2],
      [-1, 0, 1]]),
])
def test_solutions(args, expected):
    res = Solution().threeSum(args)
    res0 = Solution().threeSum0(args)
    res1 = Solution1().threeSum(args)
    assert sorted(res) == sorted(expected)
    assert sorted(res0) == sorted(expected)
    assert sorted(res1) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
