#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 14:37:52
# @Last Modified : 2020-04-26 14:37:52
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

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
