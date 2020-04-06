#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 18:34:49
# @Last Modified : 2020-04-06 18:34:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
