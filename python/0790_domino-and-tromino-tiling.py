#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有两种形状的瓷砖：一种是 2x1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。 
# 
#  
# XX  <- 多米诺
# 
# XX  <- "L" 托米诺
# X
#  
# 
#  给定 N 的值，有多少种方法可以平铺 2 x N 的面板？返回值 mod 10^9 + 7。 
# 
#  （平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。） 
# 
#  
# 示例:
# 输入: 3
# 输出: 5
# 解释: 
# 下面列出了五种不同的方法，不同字母代表不同瓷砖：
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY 
# 
#  提示： 
# 
#  
#  N 的范围是 [1, 1000] 
#  
# 
#  
#  Related Topics 动态规划

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTilings(self, N: int) -> int:
        """
        https://www.jiuzhang.com/solution/domino-and-tromino-tiling#tag-highlight-lang-python
        fi 表示铺满 2 x i 的地板, 尾端形状为 j 时的方案数, 尾端一共有三种情况:

        f[i][0] 表示尾端没有多余, 就是说一共有 2 x i 块格子
        f[i][1] 表示上面那一行多出来了一块, 就是说上面有 i + 1 个格子, 下面有 i 个格子
        f[i][2] 表示下面一行多出一块, 就是说上面有 i 个格子, 下面有 i + 1 个格子

        """
        if N < 3:
            return N

        MOD = 1000000007

        f = [[0, 0, 0] for i in range(N + 1)]
        f[0][0] = f[1][0] = f[1][1] = f[1][2] = 1
        for i in range(2, N + 1):
            # // 竖着放一块I型, 或者横着放两块I型, 或者放L型(两种方向)
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i - 2][1] + f[i - 2][2]) % MOD
            # // 在上面一行横着放一块I型, 或者放L型
            f[i][1] = (f[i - 1][0] + f[i - 1][2]) % MOD
            # // 在下面一行横着放一块I型, 或者放L型
            f[i][2] = (f[i - 1][0] + f[i - 1][1]) % MOD

        return f[N][0]
        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (3, 5),
])
def test_solutions(args, expected):
    assert Solution().numTilings(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

