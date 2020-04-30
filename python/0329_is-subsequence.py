#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 16:35:16
# @Last Modified : 2020-04-30 16:35:16
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        i = 0
        for char in t:
            if char == s[i]:
                i += 1
            if i == len(s):
                return True
        return i == len(s)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abc", t="ahbgdc"), True],
    [dict(s="axc", t="ahbgdc"), False],
])
def test_solutions(kw, expected):
    assert Solution().isSubsequence(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
