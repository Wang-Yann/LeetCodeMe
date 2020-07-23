#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-09 22:02:29
# @Last Modified : 2020-04-09 22:02:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
#  示例:
#
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#  Related Topics 回溯算法
#  👍 350 👎 0

"""
# https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
import collections
import itertools
from typing import List

import pytest


class Solution:

    def permuteUnique(self, nums):
        def backtrack(cur):
            if len(cur) == N:
                res.append(cur[:])
                return
            for i in range(N):
                # 递归树，一定要想清楚运行流程
                #     //当前值用过了 或
                # //当前值等于前一个值： 两种情况：
                # //1 nums[i-1] 没用过 说明回溯到了同一层 此时接着用num[i] 则会与 同层用num[i-1] 重复
                # //2 nums[i-1] 用过了 说明此时在num[i-1]的下一层 相等不会重复
                if is_used[i] or (i > 0 and nums[i - 1] == nums[i] and not is_used[i - 1]):
                    continue
                is_used[i] = True
                cur.append(nums[i])
                backtrack(cur)
                cur.pop()
                is_used[i] = False

        nums.sort()
        res = []
        N = len(nums)
        is_used = [False] * N
        backtrack([])
        return res


class Solution1:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in set(itertools.permutations(nums))]


class Solution2:
    def permuteUnique(self, nums):
        def backtrack(path, counter):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for x in counter:  # dont pick duplicates
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[x] += 1

        ans = []
        backtrack([], collections.Counter(nums))
        return ans


@pytest.mark.parametrize("args,expected", [
    ([1, 3, 2], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
])
def test_solutions(args, expected):
    assert sorted(Solution().permuteUnique(args)) == sorted(expected)
    assert sorted(Solution1().permuteUnique(args)) == sorted(expected)
    assert sorted(Solution2().permuteUnique(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
