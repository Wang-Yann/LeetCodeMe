#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 09:41:02
# @Last Modified : 2020-04-26 09:41:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections


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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "bcabc",
        "cbacdcbc"
    ]
    lists = [x for x in samples]
    res = [sol.removeDuplicateLetters(x) for x in lists]
    print(res)
