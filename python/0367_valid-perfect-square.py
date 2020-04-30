#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 15:38:16
# @Last Modified : 2020-04-30 15:38:16
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest
from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in (0,1):
            return True
        l,r = 1,num//2
        while l<=r:
            mid = (l+r)>>1
            if mid*mid<num:
                l=mid+1
            elif mid*mid>num:
                r=mid-1
            else:
                return True
        return False

@pytest.mark.parametrize("args,expected",[
   (16,True),
   (14,False),
   (2,False),
])
def test_solutions(args,expected):
    assert Solution().isPerfectSquare(args)==expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
