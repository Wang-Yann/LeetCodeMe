#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 17:03:09
# @Last Modified : 2020-08-04 17:03:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。 
# 
#  
# 
#  示例 1： 
# 
#  输入：Y = 1992, M = 7
# 输出：31
#  
# 
#  示例 2： 
# 
#  输入：Y = 2000, M = 2
# 输出：29
#  
# 
#  示例 3： 
# 
#  输入：Y = 1900, M = 2
# 输出：28
#  
# 
#  
# 
#  提示： 
# 
#  
#  1583 <= Y <= 2100 
#  1 <= M <= 12 
#  
#  👍 5 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif M in (4, 6, 9, 11):
            return 30
        if Y % 400 == 0 or (Y % 100 != 0 and Y % 4 == 0):
            return 29
        else:
            return 28


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(Y=1992, M=7), 31],
    [dict(Y=2000, M=2), 29],
    [dict(Y=1900, M=2), 28],
])
def test_solutions(kw, expected):
    assert Solution().numberOfDays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
