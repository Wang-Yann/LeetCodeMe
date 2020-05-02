#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 22:15:12
# @Last Modified : 2020-05-02 22:15:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        """
        当*出现时，一定会在前面跟一个其他字符，所以一定会出现在pattern[1]的位置。一种情况是我们忽略这对pattern，因为可以出现0次；
        另一种情况是匹配上这个字符，用递归的方式匹配下一个。

         一定  要用f_match = bool(s)，否则结果可能输出''
        """
        if not p:
            return not s
        f_match = bool(s) and p[0] in [s[0], "."]
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (
                    f_match and self.isMatch(s[1:], p)
            )
        else:
            return f_match and self.isMatch(s[1:], p[1:])


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="aa", p="a"), False),
    (dict(s="aa", p="a*"), True),
    (dict(s="ab", p=".*"), True),
    (dict(s="aab", p="c*a*b"), True),
    (dict(s="mississippi", p="mis*is*p*."), False),
    (dict(s="ab", p=".*c"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isMatch(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
