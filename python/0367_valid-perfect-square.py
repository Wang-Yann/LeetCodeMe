#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 15:38:16
# @Last Modified : 2020-04-30 15:38:16
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
#  说明：不要使用任何内置的库函数，如 sqrt。
#
#  示例 1：
#
#  输入：16
# 输出：True
#
#  示例 2：
#
#  输入：14
# 输出：False
#
#  Related Topics 数学 二分查找
#  👍 146 👎 0

"""


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
