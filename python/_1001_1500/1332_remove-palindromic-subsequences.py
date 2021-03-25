#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s，它仅由字母 'a' 和 'b' 组成。每一次删除操作都可以从 s 中删除一个回文 子序列。 
# 
#  返回删除给定字符串中所有字符（字符串为空）的最小删除次数。 
# 
#  「子序列」定义：如果一个字符串可以通过删除原字符串某些字符而不改变原字符顺序得到，那么这个字符串就是原字符串的一个子序列。 
# 
#  「回文」定义：如果一个字符串向后和向前读是一致的，那么这个字符串就是一个回文。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "ababa"
# 输出：1
# 解释：字符串本身就是回文序列，只需要删除一次。
#  
# 
#  示例 2： 
# 
#  输入：s = "abb"
# 输出：2
# 解释："abb" -> "bb" -> "". 
# 先删除回文子序列 "a"，然后再删除 "bb"。
#  
# 
#  示例 3： 
# 
#  输入：s = "baabb"
# 输出：2
# 解释："baabb" -> "b" -> "". 
# 先删除回文子序列 "baab"，然后再删除 "b"。
#  
# 
#  示例 4： 
# 
#  输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 1000 
#  s 仅包含字母 'a' 和 'b' 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
        因此如果s为空字符串，则需要删除0次，为回文字符串，需要删除1次，否则一次删除所有的a, 一次删除所有的b，满足条件，故为2次
        """

        def isPalindromeSub(word: str) -> bool:
            a = 0
            b = len(word) - 1
            while a <= b:
                if word[a] != word[b]:
                    return False
                a += 1
                b -= 1
            return True

        if not s:
            return 0
        if isPalindromeSub(s):
            return 1
        return 2


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(s="ababa"), 1],
    [dict(s="abb"), 2],
    [dict(s="baabb"), 2],
])
def test_solutions(kw, expected):
    assert Solution().removePalindromeSub(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
