#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 09:47:41
# @Last Modified : 2021-02-23 09:47:41
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s ，如果可以将它分割成三个 非空 回文子字符串，那么返回 true ，否则返回 false 。 
# 
#  当一个字符串正着读和反着读是一模一样的，就称其为 回文字符串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcbdd"
# 输出：true
# 解释："abcbdd" = "a" + "bcb" + "dd"，三个子字符串都是回文的。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "bcbddxy"
# 输出：false
# 解释：s 没办法被分割成 3 个回文子字符串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= s.length <= 2000 
#  s 只包含小写英文字母。 
#  
#  Related Topics 字符串 动态规划 
#  👍 12 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    dp[i, j] is the result of if substring s[i...j] is a palindrome
    """

    def checkPartitioning(self, s: str) -> bool:
        N = len(s)

        dp = [[True] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

        for i in range(1, N):
            for j in range(i + 1, N):
                if dp[0][i - 1] and dp[i][j - 1] and dp[j][N - 1]:
                    return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abcbdd"), True],
    [dict(s="bcbddxy"), False],
])
def test_solutions(kw, expected):
    assert Solution().checkPartitioning(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
