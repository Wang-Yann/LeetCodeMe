#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-09 22:02:29
# @Last Modified : 2020-04-09 22:02:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  Related Topics 回溯算法
#  👍 791 👎 0

"""

import itertools
from typing import List

import pytest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        self.dfs(res, [], nums)
        return res

    def dfs(self, result, current_list, rest_list):
        if not rest_list:
            result.append(current_list)
        else:
            for i, v in enumerate(rest_list):
                self.dfs(result, current_list + [v], rest_list[0:i] + rest_list[i + 1:])

    def permute1(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in itertools.permutations(nums, len(nums))]


class Solution1:
    def permute(self, nums):
        """
        解决一个回溯问题，实际上就是一个决策树的遍历过程
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == N:
                output.append(nums[:])
            for i in range(first, N):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        N = len(nums)
        output = []
        backtrack(0)
        return output


class Solution2(object):
    """标准思路"""

    def permute(self, num):
        result = []
        used = [False] * len(num)

        def backtrack(cur):
            if len(cur) == len(num):
                result.append(cur[:])
                return
            for i in range(len(num)):
                if used[i]:
                    continue
                used[i] = True
                cur.append(num[i])
                backtrack(cur)
                cur.pop()
                used[i] = False

        backtrack([])
        return result


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3],
     [
         [1, 2, 3],
         [1, 3, 2],
         [2, 1, 3],
         [2, 3, 1],
         [3, 1, 2],
         [3, 2, 1]
     ])
])
def test_solutions(args, expected):
    assert sorted(Solution().permute(args)) == sorted(expected)
    assert sorted(Solution().permute1(args)) == sorted(expected)
    assert sorted(Solution1().permute(args)) == sorted(expected)
    assert sorted(Solution2().permute(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
