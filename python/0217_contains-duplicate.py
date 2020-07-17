#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 12:53:32
# @Last Modified : 2020-04-06 12:53:32
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个整数数组，判断是否存在重复元素。
#
#  如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
#
#
#
#  示例 1:
#
#  输入: [1,2,3,1]
# 输出: true
#
#  示例 2:
#
#  输入: [1,2,3,4]
# 输出: false
#
#  示例 3:
#
#  输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
#  Related Topics 数组 哈希表
#  👍 268 👎 0

"""

import os
import sys
import traceback
from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        a_set=set()
        for v in nums:
            if v not in a_set:
                a_set.add(v)
            else:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    sample = [1, 2, 3, 4, 5, 6, 7]
    print(sol.containsDuplicate(sample))
