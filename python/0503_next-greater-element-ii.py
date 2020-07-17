#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 14:37:52
# @Last Modified : 2020-04-26 14:37:52
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第
# 一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
#
#  示例 1:
#
#
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
#
#
#  注意: 输入数组的长度不会超过 10000。
#  Related Topics 栈
#  👍 159 👎 0

"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        单调栈
        倒序数组存储一个单调栈
        如果当前数比栈顶小，那么栈顶一定是当前数所能发现的第一个最大值
        """
        length = len(nums)
        result = [0] * length
        stack = []

        for i in range(length * 2 - 1, -1, -1):
            idx = i % length
            while stack and stack[-1] <= nums[idx]:
                stack.pop()
            result[idx] = stack[-1] if stack else -1
            stack.append(nums[idx])
        return result


if __name__ == '__main__':
    sol = Solution()
    # [[2, -1, 2], [4, -1, 4, 4, 4],[120,11,120,120,123,123,-1,100,100,100]]
    samples = [
        [1, 2, 1],
        [1, 4, 3, 2, 1],
        [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    ]
    lists = [x for x in samples]
    res = [sol.nextGreaterElements(x) for x in lists]
    print(res)
