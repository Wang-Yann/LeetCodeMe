#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个由小写字母组成的字符串 s，和一个整数 k。 
# 
#  请你按下面的要求分割字符串： 
# 
#  
#  首先，你可以将 s 中的部分字符修改为其他的小写英文字母。 
#  接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。 
#  
# 
#  请返回以这种方式分割字符串所需修改的最少字符数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abc", k = 2
# 输出：1
# 解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
#  
# 
#  示例 2： 
# 
#  输入：s = "aabbc", k = 3
# 输出：0
# 解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。 
# 
#  示例 3： 
# 
#  输入：s = "leetcode", k = 8
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= s.length <= 100 
#  s 中只含有小写英文字母。 
#  
#  Related Topics 动态规划

"""
import sys

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        https://leetcode-cn.com/problems/palindrome-partitioning-iii/solution/fen-ge-hui-wen-chuan-iii-by-leetcode-solution/
        我们用 dp[i][j] 表示对于字符串 S 的前 i 个字符，将它分割成 j 个非空且不相交的回文串，最少需要修改的字符数
        我们可以枚举第 j 个回文串的起始位置 i0，那么就有如下的状态转移方程：
        f[i][j] = min(f[i0][j - 1] + cost(S, i0 + 1, i))
        """

        def cost(l, r):
            """
            cost(S, l, r) 表示将 S 的第 l 个到第 r 个字符组成的子串变成回文串，最少需要修改的字符数
            """
            ret = 0
            while l < r:
                if s[l] != s[r]:
                    ret += 1
                l += 1
                r -= 1
            return ret

        N = len(s)
        dp = [[sys.maxsize] * (k + 1) for _ in range(N + 1)]
        dp[0][0] = 0
        for i in range(1, N + 1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    dp[i][j] = cost(0, i - 1)
                else:
                    # print(j-1,i)
                    for i0 in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[i0][j - 1] + cost(i0, i - 1))
        return dp[N][k]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(s="abc", k=2), 1],
    [dict(s="aabbc", k=3), 0],
    [dict(s="leetcode", k=8), 0],
])
def test_solutions(kw, expected):
    assert Solution().palindromePartition(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
