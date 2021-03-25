#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。 
# 
#  示例 1: 
# 
#  
# 输入: "abab"
# 
# 输出: True
# 
# 解释: 可由子字符串 "ab" 重复两次构成。
#  
# 
#  示例 2: 
# 
#  
# 输入: "aba"
# 
# 输出: False
#  
# 
#  示例 3: 
# 
#  
# 输入: "abcabcabcabc"
# 
# 输出: True
# 
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        """KMP
        https://leetcode-cn.com/problems/repeated-substring-pattern/solution/kmp-python3jie-ti-si-lu-by-jackwener/
        """

        def get_prefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j > -1 and pattern[j + 1] != pattern[i]:
                    j = prefix[j]
                if pattern[j + 1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix
        length = len(s)
        pre = get_prefix(s)
        # print(pre)
        # length - (pre[-1] + 1) 一个字串长度
        # 如果是"abcabcabc"，那么dp数组为[-1, -1, -1, 0, 1, 2, 3, 4, 5]，我们发现最后一个数字为5，那么表示重复的字符串为“abcabc”，有5+1个字符
        # 重复字符串的长度和肯定是一个子字符串的整数倍
        return pre[-1]>=0 and length % (length - (pre[-1] + 1)) == 0


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        ss = (s + s)[1:-1]
        return s in ss


@pytest.mark.parametrize("args,expected", [
    ("abab", True),
    ("abcabcabcabc", True),
    ("abcabcabc", True),
    pytest.param("aba", False),
])
def test_solutions(args, expected):
    assert Solution().repeatedSubstringPattern(args) == expected
    assert Solution1().repeatedSubstringPattern(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
