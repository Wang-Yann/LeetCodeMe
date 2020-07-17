#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 13:32:46
# @Last Modified : 2020-04-06 13:32:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
#
#
#  示例 1:
#
#  输入: [3,0,1]
# 输出: 2
#
#
#  示例 2:
#
#  输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
#
#
#
#
#  说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
#  Related Topics 位运算 数组 数学
#  👍 285 👎 0

"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums: return 0
        length = len(nums)
        return (length + 1) * (length) // 2 - sum(nums)

    def missingNumberBit(self, nums: List[int]) -> int:
        length = len(nums)
        missing = length
        for i, v in enumerate(nums):
            missing ^= i ^ v
        return missing


if __name__ == '__main__':
    sol = Solution()
    sample = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(sol.missingNumberBit(sample))
    print(sol.missingNumberBit([]))
