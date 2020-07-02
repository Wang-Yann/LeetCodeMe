#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 09:41:02
# @Last Modified : 2020-04-26 09:41:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections

import pytest


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """Good"""
        in_stack = set()
        remaining = collections.Counter(s)
        stack = []
        for char in s:
            if char not in in_stack:
                while stack and stack[-1] > char and remaining[stack[-1]] > 0:
                    in_stack.remove(stack.pop())
                stack.append(char)
                in_stack.add(char)
            remaining[char] -= 1
        return "".join(stack)


@pytest.mark.parametrize("args,expected", [
    ("cdadabcc", "adbc"),
    ("abcd", "abcd"),
    ("ecbacba", "eacb"),
    ("leetcode", "letcod"),
])
def test_solutions(args, expected):
    assert Solution().removeDuplicateLetters(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
