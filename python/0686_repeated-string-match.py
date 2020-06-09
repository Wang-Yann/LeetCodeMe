#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。 
# 
#  举个例子，A = "abcd"，B = "cdabcdab"。 
# 
#  答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。 
# 
# 
#  注意: 
# 
#  A 与 B 字符串的长度在1和10000区间范围内。 
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        lenA, lenB = map(len, (A, B))
        if set(B) - set(A):
            return -1
        i = 1
        tmp = A
        while i <= lenB:
            if B in tmp:
                return i
            tmp += A
            i += 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A="abcd", B="bc"), 1],
    [dict(A="abcd", B="cdabcdab"), 3],
    [dict(A="a" * 36, B="a" * 1200), 34]
])
def test_solutions(kw, expected):
    assert Solution().repeatedStringMatch(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
