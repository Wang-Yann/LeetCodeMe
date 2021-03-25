#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 18:34:49
# @Last Modified : 2020-04-06 18:34:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#  candidates 中的每个数字在每个组合中只能使用一次。
#
#  说明：
#
#
#  所有数字（包括目标数）都是正整数。
#  解集不能包含重复的组合。
#
#
#  示例 1:
#
#  输入: candidates =[10,1,2,7,6,1,5], target =8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#
#  示例 2:
#
#  输入: candidates =[2,5,2,1,2], target =5,
# 所求解集为:
# [
#  [1,2,2],
#  [5]
# ]
#  Related Topics 数组 回溯算法
#  👍 310 👎 0

"""

from typing import List
import pytest


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, path, cur_target):
            if cur_target == 0:
                result.append(list(path))
            begin = idx
            while idx < N and candidates[idx] <= cur_target:
                if idx > begin and candidates[idx] == candidates[idx - 1]:
                    idx += 1
                    continue
                path.append(candidates[idx])
                dfs(idx + 1, path, cur_target - candidates[idx])
                path.pop()
                idx += 1

        N = len(candidates)
        candidates.sort()
        result = []
        dfs(0, [], target)
        return result


class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(cur_target, idx, path):
            if cur_target == 0:  # 终止条件
                result.append(path[:])
                return
            for i in range(idx, N):
                if candidates[i] > cur_target:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                # 下面调用helper时，第二个参数的位置是i+1，一定是从当前一位的下一位开始找(开始的时候写成了idx，一直无法减枝)
                helper(cur_target - candidates[i], i + 1, path)
                path.pop()  # 回溯记得恢复状态

        N = len(candidates)
        if target == 0 or N == 0:
            return []
        result = []
        candidates.sort()
        helper(target, 0, [])
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(candidates=[10, 1, 2, 7, 6, 1, 5], target=8, ),
     [
         [1, 7],
         [1, 2, 5],
         [2, 6],
         [1, 1, 6]
     ]],
    [dict(candidates=[2, 5, 2, 1, 2], target=5, ),
     [
         [1, 2, 2],
         [5]
     ]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().combinationSum2(**kw)) == sorted(expected)
    assert sorted(Solution1().combinationSum2(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
