#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-09 20:41:04
# @Last Modified : 2020-04-09 20:41:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n<=0:return []
        res = []
        # self.dfs(res_set,"",n,n)
        self.generateParenthesisRecu(res, "", n, n)
        return list(res)

    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(result, current + ")", left, right - 1)

    def dfs(self,res_set,s,ln,rn):
        if ln>rn or ln<0 or rn<0:
            return
        elif ln<rn:
            self.dfs(res_set,s+")",ln,rn-1)
            self.dfs(res_set,s+"(",ln-1,rn)
        else:
            if ln==rn==0:
                res_set.add(s)
            else:
                self.dfs(res_set,s+"(",ln-1,rn)






if __name__ == '__main__':
    sol = Solution()
    sample=13
    print(sol.generateParenthesis(sample))