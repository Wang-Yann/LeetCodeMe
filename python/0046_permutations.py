#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-09 22:02:29
# @Last Modified : 2020-04-09 22:02:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:return []
        res = []
        self.dfs(res,[],nums)
        return res

    def dfs(self,result,current_list,rest_list):
        if  not rest_list:
            result.append(current_list)
        else:
            for i,v in enumerate(rest_list):
                self.dfs(result,current_list+[v],rest_list[0:i]+rest_list[i+1:])

    def permute1(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list( x ) for x in permutations(nums,len(nums))]

    def permuteO(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)

        def backtrack(first = 0):
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

        output = []
        backtrack(0)
        return output



if __name__ == '__main__':
    sol = Solution()
    sample=[1,3,2]
    print(sol.permute(sample))
    print(sol.permute1(sample))
    print(sol.permuteO(sample))