#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作： 
# 
#  
#  Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。 
#  Paste (粘贴) : 你可以粘贴你上一次复制的字符。 
#  
# 
#  给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。 
# 
#  示例 1: 
# 
#  
# 输入: 3
# 输出: 3
# 解释:
# 最初, 我们只有一个字符 'A'。
# 第 1 步, 我们使用 Copy All 操作。
# 第 2 步, 我们使用 Paste 操作来获得 'AA'。
# 第 3 步, 我们使用 Paste 操作来获得 'AAA'。
#  
# 
#  说明: 
# 
#  
#  n 的取值范围是 [1, 1000] 。 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSteps(self, n: int) -> int:
        """
        https://leetcode-cn.com/problems/2-keys-keyboard/solution/zhi-you-liang-ge-jian-de-jian-pan-by-leetcode/
        素数分解
        假设 g_1, g_2, ... 就是 N 的素数分解，则需要的最少操作等于这些素数之和。
        将所有操作分成以 copy 为首的多组，形如 (copy, paste, ..., paste)，再使用 C 代表 copy，P 代表 paste。例如操作 CPPCPPPPCP 可以分为 [CPP][CPPPP][CP] 三组。
        假设每组的长度为 g_1, g_2, ...。完成第一组操作后，字符串有 g_1 个 A，完成第二组操作后字符串有 g_1 * g_2 个 A。
        当完成所有操作时，共有 g_1 * g_2 * ... * g_n 个 'A'

        """

        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minSteps(self, n: int) -> int:
        """
        遇到最大的因子直接复制粘贴即可。
        """
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(i - 1, 0, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break
        return dp[n]


@pytest.mark.parametrize("args,expected", [
    (3, 3)
])
def test_solutions(args, expected):
    assert Solution().minSteps(args) == expected
    assert Solution1().minSteps(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
