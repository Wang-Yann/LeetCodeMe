#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 17:02:57
# @Last Modified : 2020-07-23 17:02:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个 非空 字符串，将其编码为具有最短长度的字符串。 
# 
#  编码规则是：k[encoded_string]，其中在方括号 encoded_string 中的内容重复 k 次。 
# 
#  注： 
# 
#  
#  k 为正整数且编码后的字符串不能为空或有额外的空格。 
#  你可以假定输入的字符串只包含小写的英文字母。字符串长度不超过 160。 
#  如果编码的过程不能使字符串缩短，则不要对其进行编码。如果有多种编码方式，返回任意一种即可。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入： "aaa"
# 输出： "aaa"
# 解释： 无法将其编码为更短的字符串，因此不进行编码。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入： "aaaaa"
# 输出： "5[a]"
# 解释： "5[a]" 比 "aaaaa" 短 1 个字符。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入： "aaaaaaaaaa"
# 输出： "10[a]"
# 解释： "a9[a]" 或 "9[a]a" 都是合法的编码，和 "10[a]" 一样长度都为 5。
#  
# 
#  
# 
#  示例 4： 
# 
#  输入： "aabcaabcd"
# 输出： "2[aabc]d"
# 解释： "aabc" 出现两次，因此一种答案可以是 "2[aabc]d"。
#  
# 
#  
# 
#  示例 5： 
# 
#  输入： "abbbabbbcabbbabbbc"
# 输出： "2[2[abbb]c]"
# 解释： "abbbabbbc" 出现两次，但是 "abbbabbbc" 可以编码为 "2[abbb]c"，因此一种答案可以是 "2[2[abbb]c]"。
#  
# 
#  
#  Related Topics 动态规划 
#  👍 18 👎 0

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        res = s
        if len(s) <= 4:
            return res
        loc = (s + s).find(s, 1)
        if loc < len(s):
            res = str(len(s) // loc) + "[" + self.encode(s[:loc]) + "]"
        for i in range(1, len(s)):
            left = self.encode(s[:i])
            right = self.encode(s[i:])
            res = min(res, left + right, key=len)
        # print("s->loc->res", s,loc, res)
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def encode(self, s: str) -> str:
        """
        区间dp
        dp[i][j]表示起点为i，终点为j的区间最优解。
        首先枚举起点，枚举终点。截取当前区间字符串，利用k将当前区间分为左右两部分。如果分割的左右两部分当前最优解合并后长度小于当前区间最优解，选择更新。
        TODO
        重点理解：tmp + tmp拼接起来，然后在第一个字母后面查找，当区间内有重复字符串时，查找结果的起点不会超出区间，然后可以构造新的字符串，用来更新dp
        """
        N = len(s)
        dp = [[""] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):  # 枚举区间起点
            dp[i][i] = s[i]
            for j in range(i + 1, N):  # 枚举区间终点
                tmp = s[i: j + 1]  # 截取当前区间
                dp[i][j] = tmp

                # prefer original over compressed
                for k in range(i, j):  # 利用k分割出左部分和右部分
                    if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):  # 如果左右两侧长度和小于当前答案就更新
                        dp[i][j] = dp[i][k] + dp[k + 1][j]

                # compress whole string only for shorter length
                size = len(tmp)
                index = (tmp + tmp).find(tmp, 1)  # 1表示从拼接的字符串首字母后开始查找
                if index < size:  # 如果区间内包含重复字符串，则返回的起点不会超过区间
                    replace = "%d[%s]" % (size // index, dp[i][i + index - 1])  # 计算字符串前的数字即k
                    if len(replace) < len(dp[i][j]):  # 如果长度更小就进行更新
                        dp[i][j] = replace
        # print(dp)
        return dp[0][N - 1]


@pytest.mark.parametrize("args,expected", [
    ("aaa", ["aaa"]),
    ("aaaaa", ["5[a]"]),
    ("aaaaaaaaaa", ["10[a]", "a9[a]", "9[a]a"]),
    ("aabcaabcd", ["2[aabc]d"]),
    ("abbbabbbcabbbabbbc", ["2[2[abbb]c]"]),
])
def test_solutions(args, expected):
    assert Solution().encode(args) in expected
    assert Solution1().encode(args) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
