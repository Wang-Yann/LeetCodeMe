#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 16:34:43
# @Last Modified : 2020-04-12 16:34:43
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  Related Topics 位运算 数组 回溯算法
#  👍 659 👎 0

"""

from itertools import combinations
from typing import List


class Solution:

    def subsetsS(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        for i in range(n + 1):
            results.extend([list(x) for x in combinations(nums, i)])
        return results

    def subsetsRec(self, nums: List[int]) -> List[List[int]]:
        """ 递归"""
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            回溯
            TODO absorb
        """

        def backtrack(first, curr, k):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr,k )
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0, [],k)
        return output

    def dfs_backtrack(self, nums, output, k, n, first, curr):
        if len(curr) == k:
            output.append(curr[:])
        for i in range(first, n):
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            self.dfs_backtrack(nums, output, k, n, i + 1, curr)
            # backtrack
            curr.pop()

    def subsetsBackTrack(self, nums: List[int]) -> List[List[int]]:
        """ 回溯2"""
        output = []
        n = len(nums)
        for k in range(n + 1):
            self.dfs_backtrack(nums, output, k, n, 0, [])
        return output

    def subsetsBits(self, nums: List[int]) -> List[List[int]]:
        """
        BIT法
        """
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            print(bitmask,bin(i))

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [1, 2, 3],
        # [1, 5, 3,6],
    ]
    res = [sol.subsets(x) for x in samples]
    # res = [sol.subsetsBits(x) for x in samples]
    print(res)
