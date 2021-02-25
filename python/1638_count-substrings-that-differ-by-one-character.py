#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 03:51:18
# @Last Modified : 2021-02-25 03:51:18
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，请你找到 s 和 t 串中 
# 恰好 只有一个字符不同的子字符串对的数目。 
# 
#  比方说， "computer" 和 "computation" 加粗部分只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。 
# 
#  请你返回满足上述条件的不同子字符串对数目。 
# 
#  一个 子字符串 是一个字符串中连续的字符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aba", t = "baba"
# 输出：6
# 解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# 加粗部分分别表示 s 和 t 串选出来的子字符串。
#  
# 示例 2：
# 
#  
# 输入：s = "ab", t = "bb"
# 输出：3
# 解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# 加粗部分分别表示 s 和 t 串选出来的子字符串。
#  
# 示例 3：
# 
#  
# 输入：s = "a", t = "a"
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "abe", t = "bbc"
# 输出：10
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 100 
#  s 和 t 都只包含小写英文字母。 
#  
#  Related Topics 字典树 哈希表 字符串 
#  👍 18 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        cur is the current number of consecutive same characters.
        pre is the previous number of consecutive same characters.
        """
        s_len = len(s)
        t_len = len(t)
        res = 0

        for i in range(s_len):
            for j in range(t_len):
                diff = 0
                k = 0
                while i + k < s_len and j + k < t_len:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff > 2:
                        break
                    if diff == 1:
                        res += 1

                    k += 1
        return res



# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="aba", t="baba"), 6],
    [dict(s="ab", t="bb"), 3],
    [dict(s="a", t="a"), 0],
    [dict(s="abe", t="bbc"), 10],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countSubstrings(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
