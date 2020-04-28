#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 22:19:58
# @Last Modified : 2020-04-26 22:19:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import itertools


class Solution0:

    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            stack = []
            for char in s:
                if char != "#":
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
            return stack

        s_lst = helper(S)
        t_lst = helper(T)
        # print(s_lst,t_lst)
        return s_lst == t_lst


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper_generator(s):
            skip = 0
            length = len(s)
            for i in range(length - 1, -1, -1):
                if s[i] == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield s[i]

        for x, y in itertools.zip_longest(helper_generator(S), helper_generator(T)):
            if x != y:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(S="ab#c", T="ad#c"),
        dict(S="ab##", T="c#d#"),
        dict(S="a##c", T="#a#c"),
        dict(S="aba#cbbb", T="abbb"),
    ]
    res = [sol.backspaceCompare(**args) for args in samples]
    print(res)
