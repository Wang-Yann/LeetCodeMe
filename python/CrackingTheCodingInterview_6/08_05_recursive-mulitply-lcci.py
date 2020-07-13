#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:06:51
# @Last Modified : 2020-07-13 11:06:51
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。 
# 
#  示例1: 
# 
#  
#  输入：A = 1, B = 10
#  输出：10
#  
# 
#  示例2: 
# 
#  
#  输入：A = 3, B = 4
#  输出：12
#  
# 
#  提示: 
# 
#  
#  保证乘法范围不会溢出 
#  
#  Related Topics 递归 
#  👍 19 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A > B: A, B = B, A

        def helper(smaller, bigger):
            if smaller == 0:
                return 0
            elif smaller == 1:
                return bigger
            mid = smaller >> 1
            halfProd = helper(mid, bigger)
            if smaller % 2 == 0:
                return halfProd + halfProd
            else:
                return halfProd + halfProd + bigger

        return helper(A, B)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=1, B=10), 10],
    [dict(A=3, B=4), 12],
])
def test_solutions(kw, expected):
    assert Solution().multiply(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
