#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 22:45:44
# @Last Modified : 2020-05-01 22:45:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """GOOD"""
        d.sort(key=lambda x:(-len(x), x))
        for word in d:
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            if i == len(word):
                return word
        return ""


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="abpcplea", d=["ale", "apple", "monkey", "plea"]), "apple"),
    pytest.param(dict(s="abpcplea", d=["a", "b", "c"]), "a"),
])
def test_solutions(kwargs, expected):
    assert Solution().findLongestWord(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
