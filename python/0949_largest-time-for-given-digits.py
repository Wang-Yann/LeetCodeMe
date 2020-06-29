#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。 
# 
#  最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。 
# 
#  以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,4]
# 输出："23:41"
#  
# 
#  示例 2： 
# 
#  输入：[5,5,5,5]
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  A.length == 4 
#  0 <= A[i] <= 9 
#  
#  Related Topics 数学

"""

import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4], "23:41"),
    ([5, 5, 5, 5], ""),
])
def test_solutions(args, expected):
    assert Solution().largestTimeFromDigits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
