#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:51:51
# @Last Modified : 2020-07-11 23:51:51
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# first = "pale"
# second = "ple"
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  输入: 
# first = "pales"
# second = "pal"
# 输出: False
#  
#  Related Topics 字符串 动态规划 
#  👍 29 👎 0


"""

import math

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def oneEditAway(self, first: str, second: str) -> bool:
        """TODO"""
        len1, len2 = len(first), len(second)
        if abs(len1 - len2) > 1:
            return False
        # dp[i][j] - 字符串first[:i]和字符串second[:j]的编辑距离
        dp = [[math.inf] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[len1][len2] <= 1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(first="pale", second="ple"), True],
    [dict(first="pales", second="pal"), False],

])
def test_solutions(kwargs, expected):
    assert Solution().oneEditAway(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
