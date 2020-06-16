#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调
# 递增的。 
# 
#  我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。 
# 
#  返回使 S 单调递增的最小翻转次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入："00110"
# 输出：1
# 解释：我们翻转最后一位得到 00111.
#  
# 
#  示例 2： 
# 
#  输入："010110"
# 输出：2
# 解释：我们翻转得到 011111，或者是 000111。
#  
# 
#  示例 3： 
# 
#  输入："00011000"
# 输出：2
# 解释：我们翻转得到 00000000。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 20000 
#  S 中只包含字符 '0' 和 '1' 
#  
#  Related Topics 数组

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        """
        DP
        https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/solution/7-xing-dai-ma-chao-jian-dan-dong-tai-gui-hua-by-_f/
        对于每个字符，考虑两种情况，此字符最终状态为 0 或者 为 1，然后分别记录 0 和 1 的最少翻转次数，
        遍历完成后取最小值即为最少翻转次数
        如果 S[i] 是 '1':
        dp[i][0] = dp[i-1][0] + 1 # 只能从 0 转化来，翻转 '1' 为 '0'，翻转次数加 1
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) # 已经为 '1'，无需翻转

        如果 S[i] 是 '0':
        dp[i][0] = dp[i-1][0] # 只能从 0 转化来，无需翻转
        dp[i][1] = min(dp[i-1][0] + 1, dp[i-1][1] + 1) # 翻转 '0' 为 '1'，翻转次数加 1
        """
        zero, one = 0, 0
        for c in S:
            if c == '1':
                one, zero = min(zero, one), zero + 1
            else:
                one = min(zero + 1, one + 1)
        return min(zero, one)


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def minFlipsMonoIncr(self, S: str) -> int:
        """
        DP
        我们需要的当前最小值来自于两种途径，一种是将0,i这个区间内的元素全部变成0，另一种是将第i个元素变成1，
        而0,i这个区间内的元素按照之前的最小值取
        """
        m, n = 0, 0
        for char in S:
            # 1==>0
            m += int(char)
            n = min(m, n + (1 - int(char)))
        return n


@pytest.mark.parametrize("args,expected", [
    ("00110", 1),
    ("010110", 2),
    ("00011000", 2),
])
def test_solutions(args, expected):
    assert Solution().minFlipsMonoIncr(args) == expected
    assert Solution1().minFlipsMonoIncr(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
