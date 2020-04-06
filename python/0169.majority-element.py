#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 12:46:13
# @Last Modified : 2020-04-06 12:46:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List
from collections import Counter


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        res = Counter(nums)
        return max(res.items(),key=lambda x:x[1])[0]


if __name__ == '__main__':
    sol = Solution()
    sample = [2, 2, 1, 1, 1, 2, 2]
    print(sol.majorityElement(sample))
