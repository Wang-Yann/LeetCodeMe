#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个长度为 n 的字符串 s1 和 s2 ，以及一个字符串 evil 。请你返回 好字符串 的数目。 
# 
#  好字符串 的定义为：它的长度为 n ，字典序大于等于 s1 ，字典序小于等于 s2 ，且不包含 evil 为子字符串。 
# 
#  由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, s1 = "aa", s2 = "da", evil = "b"
# 输出：51 
# 解释：总共有 25 个以 'a' 开头的好字符串："aa"，"ac"，"ad"，...，"az"。还有 25 个以 'c' 开头的好字符串："ca"，"cc
# "，"cd"，...，"cz"。最后，还有一个以 'd' 开头的好字符串："da"。
#  
# 
#  示例 2： 
# 
#  输入：n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
# 输出：0 
# 解释：所有字典序大于等于 s1 且小于等于 s2 的字符串都以 evil 字符串 "leet" 开头。所以没有好字符串。
#  
# 
#  示例 3： 
# 
#  输入：n = 2, s1 = "gx", s2 = "gz", evil = "x"
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  s1.length == n 
#  s2.length == n 
#  s1 <= s2 
#  1 <= n <= 500 
#  1 <= evil.length <= 50 
#  所有字符串都只包含小写英文字母。 
#  
#  Related Topics 动态规划

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        """
        数位DP
        HARD HARD HARD
        这道题已经达到了竞赛的难度，即使是非常优秀的竞赛选手，也要花至少 10 分钟的时间写出完整（但不一定可读）的代码
        https://leetcode-cn.com/problems/find-all-good-strings/solution/zhao-dao-suo-you-hao-zi-fu-chuan-by-leetcode-solut/
        bound:
        如果和上下界没有任何关系，那么取值为 0，并且以后也不可能和上下界有关系；
        如果「贴着」下界，那么取值为 1，并且只有当第 pos 位取了下界对应位置的数字时，才会延续 1 值，否则会变为 0；
        如果「贴着」上界，那么取值为 1，并且只有当第  pos 位取了上界对应位置的数字时，才会延续 2 值，否则会变为 0；
        如果同时「贴着」上下界，那么取值为 3
        """

        @functools.lru_cache(None)
        def getTrans(stats, ch):
            """这是计算关于 stats 的转移函数
            输入为 stats 和 d
            输出为转移的结果 g_s(stats, d)"""

            # u = ord(ch) - 97
            # 这是 KMP 算法的一部分
            # 把 evil 看作「模式串」，stats 看作「主串」匹配到的位置
            while stats > 0 and evil[stats] != ch:
                stats = fail[stats - 1]
            return stats + 1 if evil[stats] == ch else 0

        @functools.lru_cache(None)
        def dfs(pos, stats, bound):
            """这是用来进行记忆化搜索的函数
            输入为 pos, stats 和 bound
            输出为 f[pos][stats][bound]"""

            # 如果匹配到了 evil 的末尾
            # 说明字符串不满足要求了
            # 返回 0
            if stats == len(evil):
                return 0
            # 如果匹配到了上下界的末尾
            # 说明找到了一个满足要求的字符串
            # 返回 1
            if pos == len(s1):
                return 1

            ans = 0
            # 计算第 pos 位可枚举的字符下界
            l = (ord(s1[pos]) if bound & 1 else ord('a'))
            # 计算第 pos 位可枚举的字符上界
            r = (ord(s2[pos]) if bound & 2 else ord('z'))
            for u in range(l, r + 1):
                ch = chr(u)
                nxt_stats = getTrans(stats, ch)
                # 这里写得较为复杂
                # 本质上就是关于 bound 的转移函数
                # 可以根据自己的理解编写
                nxt_bound = (ch == s1[pos] if bound & 1 else 0) ^ ((ch == s2[pos]) << 1 if bound & 2 else 0)
                ans += dfs(pos + 1, nxt_stats, nxt_bound)
            return ans % 1000000007

        m = len(evil)
        # 这是用来帮助计算关于 stats 的转移函数的 fail 数组
        fail = [0] * m
        # 这是 KMP 算法的一部分
        # 把「evil」看作模式串，得到它的 fail[] 数组
        for i in range(1, m):
            j = fail[i - 1]
            while j > 0 and evil[j] != evil[i]:
                j = fail[j - 1]
            if evil[j] == evil[i]:
                fail[i] = j + 1
        # print(fail)
        # 答案即为 f[0][0][3]
        return dfs(0, 0, 3)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=2, s1="aa", s2="da", evil="b"), 51],
    [dict(n=8, s1="leetcode", s2="leetgoes", evil="leet"), 0],
    [dict(n=2, s1="gx", s2="gz", evil="x"), 2],
])
def test_solutions(kw, expected):
    assert Solution().findGoodStrings(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
