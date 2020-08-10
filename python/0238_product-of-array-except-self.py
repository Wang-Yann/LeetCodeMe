#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 21:59:24
# @Last Modified : 2020-04-16 21:59:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之
# 外其余各元素的乘积。
#
#
#
#  示例:
#
#  输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
#
#
#  提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
#
#  说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#  进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
#  Related Topics 数组
#  👍 533 👎 0

"""

from typing import List

import pytest


class Solution:

    def productExceptSelfOf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        # print(answer)
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


class Solution1:

    def productExceptSelfOf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        left_product = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product

        return left_product


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
])
def test_solutions(args, expected):
    assert Solution().productExceptSelfOf(args) == expected
    assert Solution1().productExceptSelfOf(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
