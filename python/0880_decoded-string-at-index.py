#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 22:52:38
# @Last Modified : 2020-04-26 22:52:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def decodeAtIndex(self, S: str, K: int) -> str:
        """
        Good
        不过题目不严谨
        """
        i = 0
        for c in S:
            if c.isdigit():
                i *= int(c)
            else:
                i += 1
        print(i)
        for c in reversed(S):
            K %= i
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                i //= int(c)
            else:
                i -= 1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(S="leet2code3", K=10),
        dict(S="ha22", K=5),
        dict(S="a2345678999999999999999", K=1),
        dict(S="abc", K=1),
        dict(S="vzpp636m8y", K=2920),
        # dict(S="abc234567899999999999999999999999999999999999999999999999999999", K=2)
    ]
    res = [sol.decodeAtIndex(**args) for args in samples]
    print(res)
