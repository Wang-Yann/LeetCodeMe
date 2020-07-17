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
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
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



class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.dfs(candidates, result, 0, [], target)
        return result

    def dfs(self, candidates: List[int], result: List[List[int]],
                          start: int, intermediate: List[int], target: int) -> None:
        if target == 0:
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            self.dfs(candidates, result, start, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1


if __name__ == '__main__':
    sol = Solution()
    sample = [2, 3, 6, 7]
    print(sol.combinationSum(sample, 7))
