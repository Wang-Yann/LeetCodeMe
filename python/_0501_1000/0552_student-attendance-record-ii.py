#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。 
# 
#  学生出勤记录是只包含以下三个字符的字符串： 
# 
#  
#  'A' : Absent，缺勤 
#  'L' : Late，迟到 
#  'P' : Present，到场 
#  
# 
#  如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。 
# 
#  示例 1: 
# 
#  
# 输入: n = 2
# 输出: 8 
# 解释：
# 有8个长度为2的记录将被视为可奖励：
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# 只有"AA"不会被视为可奖励，因为缺勤次数超过一次。 
# 
#  注意：n 的值不会超过100000。 
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def checkRecord(self, n: int) -> int:
        """
        先将A排除在外， 只考虑P和L。那么此时就只有以下3种情况：
        以P结尾
        以PL结尾
        以PLL结尾
        dpi表示长度为i的字符串中不包含'A'的合法串的数量，dp(i)=dp(i-1)+dp(i-2)+dp(i-3)。
        由于字符串中只能有一个'A'，随后枚举i，假设i处为'A'，由dp(i-1) * dp(n-i)，即i处左右两侧子串数量乘积，最后加上dpn。
        """
        MOD = 10 ** 9 + 7
        dp = [0 for _ in range(n + 1)]
        dp[0]=1
        if n >= 1:
            dp[1] = 2
        if n >= 2:
            dp[2] = 4
        for i in range(3, n + 1):
            # 此处是由于i-1的字符串+"p"，i-2的字符串+"PL"，i-2的字符串+"PLL"均可构成新的i字符
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            dp[i] %= MOD
        res = 0
        for i in range(1, n + 1):
            #假设i处为'A',即i处左右两侧子串数量乘积
            res += dp[i - 1] * dp[n - i]
            res %= MOD
        return (res + dp[n]) % MOD



# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (2, 8),
])
def test_solutions(args, expected):
    assert Solution().checkRecord(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
