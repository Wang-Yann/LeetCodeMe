#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 18:34:49
# @Last Modified : 2020-04-06 18:34:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List



class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.combinationSumRecu(result, [], 1, k, n)
        return result

    def combinationSumRecu(self, result: List[List[int]], intermediate: List[int],
                          start: int, k:int, target: int) -> None:
        if k == 0 and target == 0:
            result.append(list(intermediate))
        elif k < 0:
            return
        # while start < 10 and start * k + k * (k - 1) / 2 <= target:
        while start < 10:
            intermediate.append(start)
            self.combinationSumRecu(result, intermediate, start + 1, k - 1, target - start)
            intermediate.pop()
            start += 1



if __name__ == '__main__':
    sol = Solution()
    sample = [10,1,2,7,6,1,5]
    print(sol.combinationSum3(3, 9))
