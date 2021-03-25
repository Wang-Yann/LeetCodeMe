#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 [1, k] 之间，且数组中
# 的数字都没有前导 0 。 
# 
#  给你字符串 s 和整数 k 。可能会有多种不同的数组恢复结果。 
# 
#  按照上述程序，请你返回所有可能输出字符串 s 的数组方案数。 
# 
#  由于数组方案数可能会很大，请你返回它对 10^9 + 7 取余 后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "1000", k = 10000
# 输出：1
# 解释：唯一一种可能的数组方案是 [1000]
#  
# 
#  示例 2： 
# 
#  输入：s = "1000", k = 10
# 输出：0
# 解释：不存在任何数组方案满足所有整数都 >= 1 且 <= 10 同时输出结果为 s 。
#  
# 
#  示例 3： 
# 
#  输入：s = "1317", k = 2000
# 输出：8
# 解释：可行的数组方案为 [1317]，[131,7]，[13,17]，[1,317]，[13,1,7]，[1,31,7]，[1,3,17]，[1,3,1,7
# ]
#  
# 
#  示例 4： 
# 
#  输入：s = "2020", k = 30
# 输出：1
# 解释：唯一可能的数组方案是 [20,20] 。 [2020] 不是可行的数组方案，原因是 2020 > 30 。 [2,020] 也不是可行的数组方案，因为
#  020 含有前导 0 。
#  
# 
#  示例 5： 
# 
#  输入：s = "1234567890", k = 90
# 输出：34
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5. 
#  s 只包含数字且不包含前导 0 。 
#  1 <= k <= 10^9. 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        https://leetcode-cn.com/problems/restore-the-array/solution/dong-tai-gui-hua-zhu-zi-fu-jie-xi-pan-duan-you-duo/
        """
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, N + 1):
            for j in range(i - 1, -1, -1):
                # 0不能构成数组，0只能与其前面的非0数字构成数字
                if s[j] == "0":
                    continue
                if int(s[j:i]) <= k:
                    dp[i] += dp[j]
                else:
                    # 如果当前字符是0，且与前面的第一个非0字符构成的数字大于k，那么说明往后不能再构成数字了，直接返回0
                    if s[i - 1] == "0" and dp[i] == 0:
                        return 0
                    break
            dp[i] %= MOD
        # print(dp)
        return dp[N] % MOD


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(s="1000", k=10000), 1],
    [dict(s="1000", k=10), 0],
    [dict(s="1317", k=2000), 8],
    [dict(s="2020", k=30), 1],
    [dict(s="1234567890", k=90), 34],
])
def test_solutions(kw, expected):
    assert Solution().numberOfArrays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
