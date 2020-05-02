#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 14:50:37
# @Last Modified : 2020-05-02 14:50:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import bisect
from typing import List

import pytest


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        l,r =0,length-1
        while l<=r:
            mid = (l+r)>>1
            if letters[mid]>target:
                r=mid-1
            else:
                l=mid+1
        # print(l,letters)
        return letters[l%length]



class Solution1:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters,target)
        return letters[0] if idx==len(letters) else letters[idx]


@pytest.mark.parametrize("letters", [
    (["c", "f", "j"])
])
@pytest.mark.parametrize("target,expected", [
    ("a", "c"),
    ("c", "f"),
    ("d", "f"),
    ("g", "j"),
    ("j", "c"),
    ("k", "c")
])
def test_solutions(letters, target, expected):
    assert Solution().nextGreatestLetter(letters, target, ) == expected
    assert Solution1().nextGreatestLetter(letters, target, ) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
