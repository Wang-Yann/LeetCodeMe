#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 12:53:32
# @Last Modified : 2020-04-06 12:53:32
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值
#  至多为 k。
#
#
#
#  示例 1:
#
#  输入: nums = [1,2,3,1], k = 3
# 输出: true
#
#  示例 2:
#
#  输入: nums = [1,0,1,1], k = 1
# 输出: true
#
#  示例 3:
#
#  输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
#  Related Topics 数组 哈希表
#  👍 182 👎 0

"""

from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        a_dic = dict()
        for idx, v in enumerate(nums, 0):
            if v not in a_dic:
                a_dic[v] = idx
            else:
                pre_idx = a_dic[v]
                if idx - pre_idx <= k:
                    return True
                else:
                    a_dic[v] = idx
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1, 2, 3];
    k = 2
    print(sol.containsDuplicate(nums, k))
