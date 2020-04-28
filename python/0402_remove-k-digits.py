#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 11:55:02
# @Last Modified : 2020-04-26 11:55:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """单调栈"""
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        # print("Raw res", stack)
        # - in the case k==0: return the entire list
        final_stack = stack[:-k] if k else stack
        return "".join(final_stack).lstrip("0") or "0"


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("1432219", 3),
        ("10200", 1),
        ("10", 2),

    ]
    lists = [x for x in samples]
    res = [sol.removeKdigits(*x) for x in lists]
    print(res)
