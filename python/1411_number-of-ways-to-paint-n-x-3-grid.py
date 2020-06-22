#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜
# 色不同）。 
# 
#  给你网格图的行数 n 。 
# 
#  请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1
# 输出：12
# 解释：总共有 12 种可行的方法：
# 
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出：54
#  
# 
#  示例 3： 
# 
#  输入：n = 3
# 输出：246
#  
# 
#  示例 4： 
# 
#  输入：n = 7
# 输出：106494
#  
# 
#  示例 5： 
# 
#  输入：n = 5000
# 输出：30228214
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length 
#  grid[i].length == 3 
#  1 <= n <= 5000 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numOfWays(self, n: int) -> int:
        """
        观察每一次的所有结果的最下面一行，有两种情况：

        对称的：即左右两个格子颜色相同，它将在n+1时，产生3个对称的和2个不对称的结果。
        不对称的：即左右格子颜色不同，它在n+1时，产生2个对称和2个不对称的结果。
        基础为n=1时，对称=不对称=6，然后不断迭代就可以了

        """
        MOD = 10 ** 9 + 7
        aba, abc = 6, 6
        for _ in range(1, n):
            aba, abc = (3 * aba + 2 * abc) % MOD, (2 * abc + 2 * aba) % MOD
        return (aba + abc) % MOD


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (1, 12),
    (2, 54),
    (3, 246),
    (7, 106494),
    (5000, 30228214),
])
def test_solutions(args, expected):
    assert Solution().numOfWays(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
