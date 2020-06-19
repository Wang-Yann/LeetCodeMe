#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。 
# 
#  房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。 
# 
#  假设正方形瓷砖的规格不限，边长都是整数。 
# 
#  请你帮设计师计算一下，最少需要用到多少块方形瓷砖？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 2, m = 3
# 输出：3
# 解释：3 块地砖就可以铺满卧室。
#      2 块 1x1 地砖
#      1 块 2x2 地砖 
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 5, m = 8
# 输出：5
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 11, m = 13
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 13 
#  1 <= m <= 13 
#  
#  Related Topics 动态规划 回溯算法

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        HARD
        完全背包　NP
        https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/414260/8ms-Memorized-Backtrack-Solution-without-special-case!
        The basic idea is to fill the entire block bottom up. In every step, find the lowest left unfilled square first,
         and select a square with different possible sizes to fill it. We maintain a height array (skyline) with length n while dfs.
         This skyline is the identity of the state.
        The final result we ask for is the minimum number of squares for the state [m, m, m, m, m, m, m]
        (The length of this array is n). Of course, backtrack without optimization will have a huge time complexity,
         but it can be pruned or optimized by the following three methods.
        """
        AREA = m * n

        @functools.lru_cache(None)
        def dp(state):
            # origin_state = state[:]
            if n == min(state):
                return 0
            state = list(state)
            mn = min(state)
            start = state.index(mn)
            res = AREA
            for end in range(start, m):
                if state[end] != mn:
                    break
                side = end - start + 1
                if mn + side > n:
                    break
                state[start: end + 1] = [mn + side] * side
                res = min(res, dp(tuple(state)))
            # print("state-->res", origin_state, res + 1)
            return res + 1

        if m > n:
            m, n = n, m
        return dp((0,) * m)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    # [dict(n=2, m=3), 3],
    # [dict(n=5, m=8), 5],
    [dict(n=11, m=13), 6],
])
def test_solutions(kw, expected):
    assert Solution().tilingRectangle(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
