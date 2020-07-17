#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-29 22:00:23
# @Last Modified : 2020-04-29 22:00:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
#  数学表达式如下:
#
#  如果存在这样的 i, j, k, 且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
#
#  说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#
#  示例 1:
#
#  输入: [1,2,3,4,5]
# 输出: true
#
#
#  示例 2:
#
#  输入: [5,4,3,2,1]
# 输出: false
#  👍 173 👎 0


import traceback
import pytest
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """a,b 保存两个较小数，找出一个同时大于m1和m2的数即返回。

        """
        min_num,a,b = float("inf"),float("inf"),float("inf")
        for v in nums:
            if min_num>=v:
                min_num=v
            elif b>=v:
                a,b = min_num,v
            else:
                return True
        return False



@pytest.mark.parametrize("args,expected", [
    ([1,2,3,4,5], True),
    ([5,4,3,2,1], False),
    ([2,1,5,0,4,6], True),
])
def test_solutions(args, expected):
    sol=Solution()
    assert sol.increasingTriplet(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "-v",  "--color=yes", __file__])


