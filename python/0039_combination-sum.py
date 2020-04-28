#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 18:34:49
# @Last Modified : 2020-04-06 18:34:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
