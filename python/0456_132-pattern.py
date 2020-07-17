#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 13:55:22
# @Last Modified : 2020-04-26 13:55:22
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < a
# j。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
#
#  注意：n 的值小于15000。
#
#  示例1:
#
#
# 输入: [1, 2, 3, 4]
#
# 输出: False
#
# 解释: 序列中不存在132模式的子序列。
#
#
#  示例 2:
#
#
# 输入: [3, 1, 4, 2]
#
# 输出: True
#
# 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
#
#
#  示例 3:
#
#
# 输入: [-1, 3, 2, 0]
#
# 输出: True
#
# 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
#
#  Related Topics 栈
#  👍 181 👎 0

"""

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
