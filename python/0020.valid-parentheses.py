#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 13:21:04
# @Last Modified : 2020-04-25 13:21:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def isValid(self, s: str) -> bool:
        hash_map = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c in s:
            if c in hash_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if c != hash_map[last]:
                    return False
        return  len(stack)==0


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "()", "", "()[]{}", "(]", "([)]", "{[]}"
    ]
    res = [sol.isValid(args) for args in samples]
    print(res)
