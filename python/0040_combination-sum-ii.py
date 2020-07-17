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
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
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
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
#  Related Topics 数组 回溯算法
#  👍 310 👎 0

"""

from typing import List

# prev = 0
# while start < len(candidates) and candidates[start] <= target:
#     if prev!=candidates[start]:
#         intermediate.append(candidates[start])
#         self.dfs(candidates, result, start+1, intermediate, target - candidates[start])
#         intermediate.pop()
#         prev=candidates[start]
#     start += 1

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.dfs(candidates, result, 0, [], target)
        return result

    def dfs(self, candidates: List[int], result: List[List[int]],
                          start: int, intermediate: List[int], target: int) -> None:
        if target == 0:
            result.append(list(intermediate))
        begin= start
        while start < len(candidates) and candidates[start] <= target:
            if start > begin and candidates[start]==candidates[start-1]:
                start += 1
                continue
            intermediate.append(candidates[start])
            self.dfs(candidates, result, start+1, intermediate, target - candidates[start])
            intermediate.pop()
            # prev=candidates[start]
            start += 1



if __name__ == '__main__':
    sol = Solution()
    sample = [10,1,2,7,6,1,5]
    print(sol.combinationSum2(sample, 8))
