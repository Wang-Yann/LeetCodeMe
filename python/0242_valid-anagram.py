#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 20:32:22
# @Last Modified : 2020-05-01 20:32:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections

import pytest


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution1(object):

    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)


@pytest.mark.parametrize("kw,expected", [
    (dict(s="anagram", t="nagaram"), True),
    pytest.param(dict(s="rat", t="car"), False),
])
def test_solutions(kw, expected):
    assert Solution().isAnagram(**kw) == expected
    assert Solution1().isAnagram(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
