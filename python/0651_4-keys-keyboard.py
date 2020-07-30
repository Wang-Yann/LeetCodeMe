#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 19:04:03
# @Last Modified : 2020-07-30 19:04:03
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设你有一个特殊的键盘包含下面的按键： 
# 
#  Key 1: (A)：在屏幕上打印一个 'A'。 
# 
#  Key 2: (Ctrl-A)：选中整个屏幕。 
# 
#  Key 3: (Ctrl-C)：复制选中区域到缓冲区。 
# 
#  Key 4: (Ctrl-V)：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。 
# 
#  现在，你只可以按键 N 次（使用上述四种按键），请问屏幕上最多可以显示几个 'A'呢？ 
# 
#  样例 1: 
# 
#  输入: N = 3
# 输出: 3
# 解释: 
# 我们最多可以在屏幕上显示三个'A'通过如下顺序按键：
# A, A, A
#  
# 
#  
# 
#  样例 2: 
# 
#  输入: N = 7
# 输出: 9
# 解释: 
# 我们最多可以在屏幕上显示九个'A'通过如下顺序按键：
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
#  
# 
#  
# 
#  注释: 
# 
#  
#  1 <= N <= 50 
#  结果不会超过 32 位有符号整数范围。 
#  
# 
#  
#  Related Topics 贪心算法 数学 动态规划 
#  👍 27 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxA(self, N):
        """
        要么按 'A'，要么按 'CTRL+A'，'CTRL+C' 或 'CTRL+V'。按键 N 次写出 M 个 A，只能有两种按键方式：
            加法（按 1 次）：M 加 1。
            乘法（按 k+1 次）：M 乘 k，其中 k >=2

        假设 best[k] 是按键 k 次得到 'A' 的最多数量。
        假设 k 次按键后得到了最多数量的 'A'。如果它的最后一步使用加法，则 best[k] = best[k-1] + 1。
        如果最后一步使用乘法，且乘 x，x 满足 x < k-1，则 best[k-(x+1)] = best[k-(x+1)] * x。
        当 j < k 时，根据 best[0], best[1], ..., best[k-1] 找出计算出最大的 best[k]
        """
        best = [0, 1]
        for k in range(2, N + 1):
            best.append(max(best[x] * (k - x - 1) for x in range(k - 1)))
            best[-1] = max(best[-1], best[-2] + 1)  # addition
        # print(best)
        return best[N]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def maxA(self, N: int) -> int:
        """
        连乘次数不超过 5
        """
        if N < 7:
            return N
        dp = list(range(N + 1))
        for i in range(7, N + 1):
            dp[i % 6] = max(dp[(i - 4) % 6] * 3, dp[(i - 5) % 6] * 4)
        return dp[N % 6]


@pytest.mark.parametrize("kw,expected", [
    [dict(N=3), 3],
    [dict(N=6), 6],
    [dict(N=7), 9],
])
def test_solutions(kw, expected):
    assert Solution().maxA(**kw) == expected
    assert Solution1().maxA(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
