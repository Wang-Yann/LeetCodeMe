#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 13:55:22
# @Last Modified : 2020-04-26 13:55:22
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        倒着遍历数组，维护单调减栈，当来数字大于栈顶，弹出栈顶赋予ak，相当于找到次大值，如果出现比次大小数，返回true
        """
        stack = []
        ak = float("-inf")  # 次大值,k对应值
        length = len(nums)
        for i in range(length - 1, -1, -1):
            if nums[i] < ak:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    ak = stack.pop()
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [1, 2, 3, 4],
        [3, 1, 4, 2],
        [-1, 3, 2, 0],
        [1, 0, 1, -4, -3]

    ]
    lists = [x for x in samples]
    res = [sol.find132pattern(x) for x in lists]
    print(res)
