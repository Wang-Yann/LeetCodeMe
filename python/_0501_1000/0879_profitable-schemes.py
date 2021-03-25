#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 帮派里有 G 名成员，他们可能犯下各种各样的罪行。 
# 
#  第 i 种犯罪会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。 
# 
#  让我们把这些犯罪的任何子集称为盈利计划，该计划至少产生 P 的利润。 
# 
#  有多少种方案可以选择？因为答案很大，所以返回它模 10^9 + 7 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：G = 5, P = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释： 
# 至少产生 3 的利润，该帮派可以犯下罪 0 和罪 1 ，或仅犯下罪 1 。
# 总的来说，有两种方案。
#  
# 
#  示例 2: 
# 
#  输入：G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：
# 至少产生 5 的利润，只要他们犯其中一种罪就行，所以该帮派可以犯下任何罪行 。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= G <= 100 
#  0 <= P <= 100 
#  1 <= group[i] <= 100 
#  0 <= profit[i] <= 100 
#  1 <= group.length = profit.length <= 100 
#  
# 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        """
        自底向上

        """
        dp = [[0 for _ in range(G + 1)] for _ in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in reversed(range(P + 1)):
                for j in reversed(range(G-g + 1)):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        # print(dp)
        return sum(dp[P]) % (10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        G=5, P=3, group=[2, 2], profit=[2, 3]
    ), 2),
    pytest.param(dict(G=10, P=5, group=[2, 3, 5], profit=[6, 7, 8]), 7),
])
def test_solutions(kwargs, expected):
    assert Solution().profitableSchemes(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
