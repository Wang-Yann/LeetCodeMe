#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一条包含字母 A-Z 的消息通过以下的方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  除了上述的条件以外，现在加密字符串可以包含字符 '*'了，字符'*'可以被当做1到9当中的任意一个数字。 
# 
#  给定一条包含数字和字符'*'的加密信息，请确定解码方法的总数。 
# 
#  同时，由于结果值可能会相当的大，所以你应当对109 + 7取模。（翻译者标注：此处取模主要是为了防止溢出） 
# 
#  示例 1 : 
# 
#  输入: "*"
# 输出: 9
# 解释: 加密的信息可以被解密为: "A", "B", "C", "D", "E", "F", "G", "H", "I".
#  
# 
#  示例 2 : 
# 
#  输入: "1*"
# 输出: 9 + 9 = 18（翻译者标注：这里1*可以分解为1,* 或者当做1*来处理，所以结果是9+9=18）
#  
# 
#  说明 : 
# 
#  
#  输入的字符串长度范围是 [1, 105]。 
#  输入的字符串只会包含字符 '*' 和 数字'0' - '9'。 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        分情况讨论
        dp[i] 表示字符串 s 前 i 个字符的编码数量
        """
        M = 10 ** 9 + 7
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        if s[0] == "*":
            dp[1] = 9
        elif s[0] != "0":
            dp[1] = 1
        for i in range(1, length):
            if s[i] == "*":
                dp[i + 1] = 9 * dp[i]
                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % M
                elif s[i - 1] == "2":
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % M
                elif s[i - 1] == "*":
                    dp[i + 1] = (dp[i + 1] + (6 + 9) * dp[i - 1]) % M
            else:
                dp[i + 1] = dp[i] if s[i] != "0" else 0
                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M
                elif s[i - 1] == "2" and s[i] <= "6":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M
                elif s[i - 1] == "*":
                    if s[i] <= "6":
                        dp[i + 1] = (dp[i + 1] + 2 * dp[i - 1]) % M
                    else:
                        dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M
        return dp[length]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("*", 9),
    ("1*", 18),
    ("111", 3),
    ("*1", 11),
])
def test_solutions(args, expected):
    assert Solution().numDecodings(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
