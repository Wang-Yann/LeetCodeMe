#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 10:34:59
# @Last Modified : 2020-04-26 10:34:59
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import NestedInteger


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        """TODO"""
        if not s:
            return NestedInteger()
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        # 查找数字
        i = 0
        for j in range(len(s)):
            if s[j] == "[":
                stack += [NestedInteger()]
                i = j + 1
            elif s[j] in ",]":
                if s[j - 1].isdigit():
                    stack[-1].add(NestedInteger(int(s[i:j])))
                # 此时为嵌套列表
                if s[j] == "]" and len(stack) > 1:
                    cur = stack.pop()
                    stack[-1].add(cur)
                i = j + 1

        return stack[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.deserialize("[1]"))
