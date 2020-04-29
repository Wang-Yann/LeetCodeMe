#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 17:23:31
# @Last Modified : 2020-04-29 17:23:31
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import os
import sys
import traceback
import pytest
from typing import List

def isBadVersion(v):
    return v>=4

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=1,n
        while l<=r:
            mid = (l+r)>>1
            if  isBadVersion(mid):
                r=mid-1
            else:
                l=mid+1
        return l



@pytest.mark.parametrize("args,expected", [
    (5, 4),
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.firstBadVersion(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])


