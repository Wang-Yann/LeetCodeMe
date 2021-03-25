#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
#  Related Topics 字符串 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        https://leetcode-cn.com/problems/decode-ways/solution/c-wo-ren-wei-hen-jian-dan-zhi-guan-de-jie-fa-by-pr/
        译码　仅与前两项相关
        HARD
        """
        length = len(s)
        if length == 0 or s[0] == "0":
            return 0
        # //dp[-1] = dp[0] = 1
        dp = [1] * (length + 1)
        # // 存储的是 dp[i + 1] 是 s[i] 的解码数量， 之所以是 dp[i + 1] ， 是为了防止开始循环时 f(i-2) 出现访问越界
        for idx in range(1, length):
            if s[idx] == "0":
                if s[idx - 1] in "12":
                    dp[idx + 1] = dp[idx - 1]
                else:
                    # // 非法字符串， 无解
                    return 0
            else:
                if (s[idx - 1] == "1" and "1" <= s[idx] <= "9") or (
                        s[idx - 1] == "2" and "1" <= s[idx] <= "6"):
                    dp[idx + 1] = dp[idx - 1] + dp[idx]
                else:
                    dp[idx + 1] = dp[idx]

        return dp[length]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0":
            return 0
        prev, prev_prev = 1, 0
        for i in range(len(s)):
            cur = 0
            if s[i] != "0":
                cur = prev
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                cur += prev_prev
            prev, prev_prev = cur, prev
        return prev


@pytest.mark.parametrize("args,expected", [
    ("12", 2),
    ("226", 3),
    ("0", 0),
    ("10", 1),
])
def test_solutions(args, expected):
    assert Solution().numDecodings(args) == expected
    assert Solution1().numDecodings(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
