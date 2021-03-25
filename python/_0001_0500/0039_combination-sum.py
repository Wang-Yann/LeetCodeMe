#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 18:34:49
# @Last Modified : 2020-04-06 18:34:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#  candidates 中的数字可以无限制重复被选取。
#
#  说明：
#
#
#  所有数字（包括 target）都是正整数。
#  解集不能包含重复的组合。
#
#
#  示例 1：
#
#  输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
#
#
#  示例 2：
#
#  输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
# ]
#
#
#
#  提示：
#
#
#  1 <= candidates.length <= 30
#  1 <= candidates[i] <= 200
#  candidate 中的每个元素都是独一无二的。
#  1 <= target <= 500
#
#  Related Topics 数组 回溯算法
#  👍 763 👎 0

"""

from typing import List

import pytest


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, path, cur_target):
            if cur_target == 0:
                result.append(list(path))
            while start < len(candidates) and candidates[start] <= cur_target:
                path.append(candidates[start])
                dfs(start, path, cur_target - candidates[start])
                path.pop()
                start += 1

        candidates.sort()
        result = []
        dfs(0, [], target)
        return result


class Solution1:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, path, cur_target):
            if idx == N:
                return
            if cur_target == 0:
                result.append(path[:])
                return
                # // 直接跳过
            dfs(idx + 1, path, cur_target)
            # // 选择当前数
            if candidates[idx] <= cur_target:
                path.append(candidates[idx])
                dfs(idx, path, cur_target - candidates[idx])
                path.pop()

        N = len(candidates)
        candidates.sort()
        result = []
        dfs(0, [], target)
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(candidates=[2, 3, 6, 7], target=7),
     [
         [7],
         [2, 2, 3]
     ]],
    [dict(candidates=[2, 3, 5], target=8, ),
     [
         [2, 2, 2, 2],
         [2, 3, 3],
         [3, 5]
     ]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().combinationSum(**kw)) == sorted(expected)
    assert sorted(Solution1().combinationSum(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
