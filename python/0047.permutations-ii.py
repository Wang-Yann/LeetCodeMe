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

    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        return [list( x ) for x in combinations(nums,len(nums))]

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        length=len(nums)
        is_used =[False]*length
        self.dfs(res,is_used,[], nums,length)
        return res

    def dfs(self,result,is_used,cur,nums,numslen):
        if len(cur)==numslen:
            result.append(cur[:])
        else:
            for i in range(numslen):
            #     //当前值用过了 或
            # //当前值等于前一个值： 两种情况：
            # //1 nums[i-1] 没用过 说明回溯到了同一层 此时接着用num[i] 则会与 同层用num[i-1] 重复
            # //2 nums[i-1] 用过了 说明此时在num[i-1]的下一层 相等不会重复
                if is_used[i] or (i>0 and nums[i-1]==nums[i] and not is_used[i-1]):
                    continue
                is_used[i]=True
                cur.append(nums[i])
                self.dfs(result,is_used,cur, nums,numslen)
                cur.pop()
                is_used[i]=False


if __name__ == '__main__':
    sol = Solution()
    sample=[1,3,2]
    sample=[1,1,2]
    print(sol.permuteUnique(sample))
