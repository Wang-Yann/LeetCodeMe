#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-08 22:47:01
# @Last Modified : 2020-04-08 22:47:01
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:


    def jump(self, nums: List[int]) -> int:
        cnt = 0
        reachable = 0
        curr_reachable = 0
        for i,v in enumerate(nums):
            if i> reachable:return -1
            if i>curr_reachable:
                curr_reachable = reachable
                cnt+=1
            reachable = max(reachable ,i+v)
        return cnt

@pytest.mark.parametrize("args,expected", [
    ([8,2,4,4,4,9,5,2,5,8,8,0,0,0,3,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5], 14),
    ([2,3,1,1,4], 2),
    pytest.param([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6], -1),
])
def test_solutions(args, expected):
    assert Solution().jump(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

