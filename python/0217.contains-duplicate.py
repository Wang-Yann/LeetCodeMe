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

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        a_set=set()
        for v in nums:
            if v not in a_set:
                a_set.add(v)
            else:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    sample = [1, 2, 3, 4, 5, 6, 7]
    print(sol.containsDuplicate(sample))
