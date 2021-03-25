#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 20:58:05
# @Last Modified : 2020-04-16 20:58:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回
#  0。
#
#  示例:
#
#  输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
#
#  进阶:
#
#  如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#  Related Topics 数组 双指针 二分查找

"""

from typing import List

import pytest


class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        初始化  left 指向 0 且初始化 sum 为 0
        遍历 nums 数组：
        将 [i]nums[i] 添加到 sum
        当 sum 大于等于 ss 时：
        更新 ans=min(ans,i+1−left) ，其中 i+1-i+1−left是当前子数组的长度
        然后我们可以移动左端点，因为以它为开头的满足   sum≥s 条件的最短子数组已经求出来了
        将 sum 减去 nums[left] 然后增加 left

        """
        start = 0
        sum_val = 0
        min_size = float("inf")
        for i in range(len(nums)):
            sum_val += nums[i]
            while sum_val >= s:
                min_size = min(min_size, i - start + 1)
                sum_val -= nums[start]
                start += 1
        return min_size if min_size != float("inf") else 0


@pytest.mark.parametrize("kw,expected", [
    [dict(s=7, nums=[2, 3, 1, 2, 4, 3]), 2],
])
def test_solutions(kw, expected):
    assert Solution().minSubArrayLen(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
