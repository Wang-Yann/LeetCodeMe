#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-18 23:35:08
# @Last Modified : 2020-08-18 23:35:08
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子： 
# 
#  
#  吃掉一个橘子。 
#  如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。 
#  如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。 
#  
# 
#  每天你只能从以上 3 种方案中选择一种方案。 
# 
#  请你返回吃掉所有 n 个橘子的最少天数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 10
# 输出：4
# 解释：你总共有 10 个橘子。
# 第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
# 第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
# 第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
# 第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
# 你需要至少 4 天吃掉 10 个橘子。
#  
# 
#  示例 2： 
# 
#  输入：n = 6
# 输出：3
# 解释：你总共有 6 个橘子。
# 第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
# 第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
# 第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
# 你至少需要 3 天吃掉 6 个橘子。
#  
# 
#  示例 3： 
# 
#  输入：n = 1
# 输出：1
#  
# 
#  示例 4： 
# 
#  输入：n = 56
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2*10^9 
#  
#  Related Topics 动态规划 
#  👍 22 👎 0
	 

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minDays(self, n: int) -> int:
        """AC"""

        @functools.lru_cache(None)
        def dp(cnt):
            if cnt == 1:
                return 1
            elif cnt == 2:
                return 2
            elif cnt == 3:
                return 2
            ans = cnt
            if cnt % 3 == 0:
                ans = min(ans, 1 + dp(cnt - 2 * cnt // 3))
            elif cnt % 3 == 1:
                ans = min(ans, 1 + dp(cnt - 1))
            elif cnt % 3 == 2:
                ans = min(ans, 2 + dp(cnt - 2))

            if cnt % 2 == 0:
                ans = min(ans, 1 + dp(cnt // 2))
            else:
                ans = min(ans, 1 + dp(cnt - 1))

            return ans

        return dp(n)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def minDays(self, n: int) -> int:
        @functools.lru_cache(None)
        def f(m):
            if m < 2:
                return m
            return min(f(m // 3) + m % 3, f(m // 2) + m % 2) + 1

        return f(n)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=10), 4],
    [dict(n=6), 3],
    [dict(n=1), 1],
    [dict(n=56), 6],
    [dict(n=69652), 19],

])
def test_solutions(kwargs, expected):
    assert Solution().minDays(**kwargs) == expected
    assert Solution1().minDays(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
