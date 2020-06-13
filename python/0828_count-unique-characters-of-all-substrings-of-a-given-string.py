#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。 
# 
#  例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueCh
# ars(s) = 5 。 
# 
#  本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。注意，某些子字符串可能是重复的，
# 但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。 
# 
#  由于答案可能非常大，请将结果 mod 10 ^ 9 + 7 后再返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入: "ABC"
# 输出: 10
# 解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
#      其中，每一个子串都由独特字符构成。
#      所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
#  
# 
#  示例 2： 
# 
#  输入: "ABA"
# 输出: 8
# 解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
#  
# 
#  示例 3： 
# 
#  输入：s = "LEETCODE"
# 输出：92
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 10^4 
#  s 只包含大写英文字符 
#  
#  Related Topics 双指针

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def uniqueLetterString(self, s: str) -> int:
        """
        考虑字母 "A"，并且有 S[10] = S[14] = S[20] = "A"，我们可以计算出仅包含 S[14] 的子串个数为 4 * 6 = 24，其中 4 表示子串的开始位置可以选择 11, 12, 13, 14，6 表示子串的结束位置可以选择 14, 15, 16, 17, 18, 19，根据乘法原理，子串的个数为 24

        """
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)
        ans = 0
        for A in index.values():
            A = [-1] + A + [len(s)]
            for i in range(1, len(A) - 1):
                ans += (A[i] - A[i - 1]) * (A[i + 1] - A[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("ABC", 10),
    ("ABA", 8),
    ("LEETCODE", 92),
])
def test_solutions(args, expected):
    assert Solution().uniqueLetterString(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
