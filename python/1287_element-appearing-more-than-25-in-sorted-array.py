#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。 
# 
#  请你找到并返回这个整数 
# 
#  
# 
#  示例： 
# 
#  
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^4 
#  0 <= arr[i] <= 10^5 
#  
#  Related Topics 数组

"""

import bisect
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        span = N // 4 + 1
        for i in range(0, N, span):
            iter_l = bisect.bisect_left(arr, arr[i])
            iter_r = bisect.bisect_right(arr, arr[i])
            # print(i,arr[i],iter_l,iter_r)
            if iter_r - iter_l >= span:
                return arr[i]
        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]), 6],
])
def test_solutions(kw, expected):
    assert Solution().findSpecialInteger(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
