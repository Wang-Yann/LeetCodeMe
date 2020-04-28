#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 12:53:32
# @Last Modified : 2020-04-06 12:53:32
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        a_dic = dict()
        for idx, v in enumerate(nums, 0):
            if v not in a_dic:
                a_dic[v] = idx
            else:
                pre_idx = a_dic[v]
                if idx - pre_idx <= k:
                    return True
                else:
                    a_dic[v] = idx
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,1,2,3]; k = 2
    print(sol.containsDuplicate(nums,k))
