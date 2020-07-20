#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 23:27:53
# @Last Modified : 2020-05-04 23:27:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
#
#
#  示例：
#
#  输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  1 <= nums[i] <= 10000
#
#  👍 33 👎 0


import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        def helper(nums,func):
            if  len(nums)==0:
                return []
            l,r =0,len(nums)-1
            while  l<r:
                while l<r and not func(nums[l]):
                    l+=1
                while  l<r and func(nums[r]):
                    r-=1
                if l<r:
                    nums[l],nums[r] =nums[r],nums[l]
            return nums
        is_even = lambda x:x&1==0
        return  helper(nums,is_even)





@pytest.mark.parametrize("args,expected", [
    ([1,2,3,4], [ [1,3,2,4], [3,1,2,4]]),
])
def test_solutions(args, expected):
    assert Solution().exchange(args) in expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


