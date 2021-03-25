#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:30:54
# @Last Modified : 2020-05-05 17:30:54
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重
# 复。
#
#  给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
#
#  示例 1:
#
#
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
#
#
#  注意:
#
#
#  给定数组的长度范围是 [2, 10000]。
#  给定的数组是无序的。
#
#  Related Topics 哈希表 数学
#  👍 98 👎 0

"""
from typing import List

import pytest


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        arr = [0] * (N + 1)
        dup, missing = -1, 1
        for v in nums:
            arr[v] += 1
        for i in range(1, N + 1):
            if arr[i] == 0:
                missing = i
            elif arr[i] == 2:
                dup = i
        return [dup, missing]


class Solution1(object):
    def findErrorNums(self, nums):
        x_xor_y = 0
        for i in range(len(nums)):
            x_xor_y ^= nums[i] ^ (i + 1)
        bit = x_xor_y & ~(x_xor_y - 1)
        result = [0] * 2
        for i, num in enumerate(nums):
            result[bool(num & bit)] ^= num
            result[bool((i + 1) & bit)] ^= i + 1
        if result[0] not in nums:
            result[0], result[1] = result[1], result[0]
        return result


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 2, 4], [2, 3]),
    ([1, 1], [1, 2]),
])
def test_solutions(args, expected):
    assert Solution().findErrorNums(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
