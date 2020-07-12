#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:58:38
# @Last Modified : 2020-07-12 21:58:38
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 插入。给定两个32位的整数N与M，以及表示比特位置的i与j。编写一种方法，将M插入N，使得M从N的第j位开始，到第i位结束。假定从j位到i位足以容纳M，也即
# 若M = 10 011，那么j和i之间至少可容纳5个位。例如，不可能出现j = 3和i = 2的情况，因为第3位和第2位之间放不下M。 
# 
#  示例1: 
# 
#  
#  输入：N = 10000000000, M = 10011, i = 2, j = 6
#  输出：N = 10001001100
#  
# 
#  示例2: 
# 
#  
#  输入： N = 0, M = 11111, i = 0, j = 4
#  输出：N = 11111
#  
#  Related Topics 位运算 
#  👍 11 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        """
        将N 的[i, j]位都置零
        再将M和N的i位开始与
        """
        for k in range(i, j + 1):
            N &= ~(1 << k)
        return N | (M << i)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(N=0b10000000000, M=0b10011, i=2, j=6), 0b10001001100],

    pytest.param(dict(N=0, M=11111, i=0, j=4), 11111),
])
def test_solutions(kwargs, expected):
    assert Solution().insertBits(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
