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
import functools

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

class Solution1(object):
    """
    每个操作都算一个步骤，给了我们一个数字N，问我们N个操作最多能输出多个A。
    我们可以分析题目中的例子可以发现，N步最少都能打印N个A出来，因为我们可以每步都是打印A。
    那么能超过N的情况肯定就是使用了复制粘贴，这里由于全选和复制要占用两步，所以能增加A的个数的操作其实只有N-2步，
    那么我们如何确定打印几个A，剩下都是粘贴呢，其实是个trade off，A打印的太多或太少，都不会得到最大结果，
    所以打印A和粘贴的次数要接近，最简单的方法就是遍历所有的情况然后取最大值，打印A的次数在[1, N-3]之间，
    粘贴的次数为N-2-i，加上打印出的部分，就是N-1-i了
    """

    @functools.lru_cache(None)
    def maxA(self, N):
        res = N
        for i in range(1, N - 2):
            res = max(res, self.maxA(i) * ((N - 2 - i) + 1))
        return res


class Solution2:
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


class Solution00(object):
    """
    TLE
    第⼀个状态是剩余的按键次数，⽤ n 表⽰；
    第⼆个状态是当前屏幕上字符 A 的数量，⽤ a_num 表⽰；
    第三个状态 是剪切板中字符 A 的数量，⽤ copy_num 表⽰。

    """

    def maxA(self, N):
        @functools.lru_cache(None)
        def dp(n, a_num, copy_num):
            if n <= 0:
                return a_num
            return max(
                dp(n - 1, a_num + 1, copy_num),  # A
                dp(n - 1, a_num + copy_num, copy_num),  # C-v
                dp(n - 2, a_num, a_num),  # C-A,C-c
            )

        return dp(N, 0, 0)


class Solution01:
    def maxA(self, N: int) -> int:
        """
        dp(n)　n为剩余敲击次数
        """
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            # 按下A键盘
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                # // 全选 & 复制 dp[j-2]，连续粘贴 i - j 次, 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[N]


@pytest.mark.parametrize("kw,expected", [
    [dict(N=3), 3],
    [dict(N=6), 6],
    [dict(N=7), 9],
    [dict(N=39), 65536],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1, Solution2,
                                         Solution00, Solution01])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxA(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
