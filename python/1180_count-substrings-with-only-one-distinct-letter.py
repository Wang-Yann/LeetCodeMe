#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 13:54:01
# @Last Modified : 2020-08-05 13:54:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 S，返回只含 单一字母 的子串个数。 
# 
#  示例 1： 
# 
#  输入： "aaaba"
# 输出： 8
# 解释： 
# 只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
# "aaa" 出现 1 次。
# "aa" 出现 2 次。
# "a" 出现 4 次。
# "b" 出现 1 次。
# 所以答案是 1 + 2 + 4 + 1 = 8。
#  
# 
#  示例 2: 
# 
#  输入： "aaaaaaaaaa"
# 输出： 55
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 1000 
#  S[i] 仅由小写英文字母组成。 
#  
#  Related Topics 数学 字符串 
#  👍 12 👎 0

"""

import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countLetters(self, S: str) -> int:
        """AC"""
        ans = 0
        for char, grp in itertools.groupby(S):
            l = len(list(grp))
            ans += sum(range(l + 1))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def countLetters(self, S):

        result = len(S)
        left = 0
        for right in range(1, len(S)):
            if S[right] == S[left]:
                result += right - left
            else:
                left = right
        return result


@pytest.mark.parametrize("args,expected", [
    ("aaaba", 8),
    ("aaaaaaaaaa", 55),
])
def test_solutions(args, expected):
    assert Solution().countLetters(args) == expected
    assert Solution1().countLetters(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
